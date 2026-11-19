# ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗
# ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
# ██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
# ██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
# ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
# ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
# REAPER PORT SCANNER
# Made By MarkDevBrasil
# My GitHub: https://github.com/MarkDevBrasil

# Serviços Pre-Configurados (Nome de portas especificas)

SERVICOS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    3389: "RDP",
}

PORTAS_UDP = {
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    123: "NTP",
    161: "SNMP",
    500: "ISAKMP",
    503: "IPSEC",
    1900: "SSDP",
    5353: "DNS",
}

# Portas Web (HTTP/HTTPS) Pre-Configuradas
PORTAS_HTTP = [
    80,
    443,
]

# Bibliotecas
import socket
import ssl
import sys
from concurrent.futures import ThreadPoolExecutor
import argparse


# Função para escanear uma porta UDP específica em um alvo
# Retorna uma string com o resultado, ou None se a porta estiver fechada.
def scan_porta_udp(alvo, porta, timeout=0.2):
    servico = PORTAS_UDP.get(porta, "Desconhecido")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(timeout)
            s.sendto(b"", (alvo, porta))
            s.recvfrom(1024)
            # Recebeu resposta: a porta está realmente aberta
            return f" Porta {porta}/udp ABERTA - Serviço: {servico}"
    except socket.timeout:
        # Em UDP, ausência de resposta NÃO significa fechada:
        # a porta pode estar aberta ou filtrada por firewall.
        return f" Porta {porta}/udp ABERTA|FILTRADA - Serviço: {servico}"
    except ConnectionRefusedError:
        # ICMP "port unreachable": porta fechada
        return None
    except OSError:
        return None


# Função para escanear uma porta TCP específica em um alvo
def scan_porta(alvo, porta, timeout=0.2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        resultado = s.connect_ex((alvo, porta))

    if resultado == 0:
        servico = SERVICOS.get(porta, "Desconhecido")
        return f" Porta {porta}/tcp ABERTA - Serviço: {servico}"
    return None


# Função para escanear uma porta HTTP específica em um alvo
# (antes era uma cópia idêntica de scan_porta; agora faz uma requisição HTTP
# e mostra o status e o cabeçalho Server)
def scan_porta_http(alvo, porta, timeout=0.2, host=None):
    host = host or alvo
    timeout = max(timeout, 1.0)  # HTTP/TLS precisa de mais tempo que um connect
    try:
        with socket.create_connection((alvo, porta), timeout=timeout) as sock:
            if porta == 443:
                contexto = ssl.create_default_context()
                contexto.check_hostname = False
                contexto.verify_mode = ssl.CERT_NONE
                sock = contexto.wrap_socket(sock, server_hostname=host)

            requisicao = f"HEAD / HTTP/1.0\r\nHost: {host}\r\nConnection: close\r\n\r\n"
            sock.sendall(requisicao.encode())
            dados = sock.recv(4096).decode(errors="ignore")
    except (OSError, ssl.SSLError):
        return None

    linhas = dados.splitlines()
    status = linhas[0] if linhas else "sem resposta HTTP"
    server = next(
        (l.split(":", 1)[1].strip() for l in linhas if l.lower().startswith("server:")),
        "Desconhecido",
    )
    return f" Porta {porta}/tcp HTTP - Status: {status} | Server: {server}"


# Argumentos
parser = argparse.ArgumentParser(
    description="REAPER PORT SCANNER"
)
# Adicionar novos argumentos
parser.add_argument(
    "alvo",
    help="Ip ou dominio do alvo"
)

parser.add_argument(
    "--porta",
    "-p",
    type=int,
    help="Porta específica para escanear (padrão: varre todas as portas TCP)"
)

parser.add_argument(
    "--timeout",
    "-t",
    type=float,
    default=0.2,
    help="Tempo de timeout em segundos para cada scan (padrão: 0.2)"
)


# Função para informar os dados de um alvo para realizar o scan
def scan(args):
    alvo_original = args.alvo
    timeout = args.timeout

    # Resolve o domínio uma única vez (evita DNS em cada thread e erros silenciosos)
    try:
        alvo = socket.gethostbyname(alvo_original)
    except socket.gaierror:
        print(f"Erro: não foi possível resolver '{alvo_original}'")
        sys.exit(1)

    # define as portas a serem escaneadas, caso não seja especificada uma porta, ele varre todas as portas
    portas = range(1, 65536)
    portas_udp = list(PORTAS_UDP)  # UDP varre só as portas conhecidas (varrer 65535 é lento e impreciso)
    portas_http = PORTAS_HTTP

    if args.porta is not None:  # "is not None" para não ignorar valores falsy
        portas = range(args.porta, args.porta + 1)
        portas_udp = [args.porta]
        portas_http = [p for p in PORTAS_HTTP if p == args.porta]

    print(f"Iniciando o scan em {alvo_original} ({alvo})")

    futuros = []
    # Informa o limite maximo e threads para o scan de uma porta
    with ThreadPoolExecutor(max_workers=100) as executor:
        for porta in portas:
            futuros.append(executor.submit(scan_porta, alvo, porta, timeout))

        # chama a função scan_porta_udp para as portas UDP
        for porta in portas_udp:
            futuros.append(executor.submit(scan_porta_udp, alvo, porta, timeout))

        # chama a função scan_porta_http para as portas web
        for porta_http in portas_http:
            futuros.append(executor.submit(scan_porta_http, alvo, porta_http, timeout, alvo_original))

    # Imprime em ordem determinística, depois que tudo terminou
    for futuro in futuros:
        resultado = futuro.result()
        if resultado:
            print(resultado)

    print("Scan finalizado")


# Chamando a função
if __name__ == "__main__":
    args = parser.parse_args()

    if args.porta is not None and not (1 <= args.porta <= 65535):
        parser.error("a porta deve estar entre 1 e 65535")
    if args.timeout <= 0:
        parser.error("o timeout deve ser maior que 0")

    try:
        scan(args)
    except KeyboardInterrupt:
        print("\nScan interrompido pelo usuário")
        sys.exit(1)
