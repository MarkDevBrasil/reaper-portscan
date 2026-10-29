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
    53 : "DNS",
    67 : "DHCP",
    68 : "DHCP",
    123 : "NTP",
    161 : "SNMP",
    500 : "ISAKMP",
    503 : "IPSEC",
    1900 : "SSDP",
    5353 : "DNS",
}

# Portas Web (HTTP/HTTPS) Pre-Configuradas
PORTAS_HTTP = [
    80,
    443,
]

# Bibliotecas
import socket
from concurrent.futures import ThreadPoolExecutor
import argparse

# Função para escanear uma porta específica em um alvo


def scan_porta_udp(alvo, porta, timeout=0.2):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(timeout)
            s.sendto(b"", (alvo, porta))
            resposta, endereco = s.recvfrom(1024)
            print(f"Porta {porta}/udp aberta")
    except socket.timeout:
        print(f"Porta {porta}/udp fechada")
    except socket.error:
        print(f"Porta {porta}/udp fechada")


def scan_porta(alvo, porta, timeout=0.2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)

        resultado = s.connect_ex((alvo, porta))

    if resultado == 0:
        serviço = SERVICOS.get(porta, "Desconhecido")
        print(f" Porta {porta}/tcp ABERTA - Serviço: {serviço}")


# Função para escanear uma porta HTTP específica em um alvo

def scan_porta_http(alvo, porta, timeout=0.2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)

        resultado = s.connect_ex((alvo, porta))

    if resultado == 0:
        serviço = SERVICOS.get(porta, "Desconhecido")
        print(f" Porta {porta}/tcp ABERTA - Serviço: {serviço}")


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
    help="Porta específica para escanear (padrão: varre todas as portas)"
)

parser.add_argument(
    "--timeout",
    "-t",
    type=float,
    default=0.2,
    help="Tempo de timeout em segundos para cada scan (padrão: 0.2)"
)

args = parser.parse_args()

# Função para informar os dados de um alvo para realizar o scan
def scan():
    alvo = args.alvo
    timeout = args.timeout

    portas = range(1, 65536)

    if args.porta:
        portas = range(args.porta, args.porta + 1)

    print("Iniciando o scan")

# Informa o limite maximo e threads para o scan de uma porta
    with ThreadPoolExecutor(max_workers=100) as executor:
        for porta in portas:
            executor.submit(scan_porta, alvo, porta, timeout)

        for porta in portas:
            executor.submit(scan_porta_udp, alvo, porta, timeout)

# Informa o limite maximo e threads para o scan de uma porta http
        for porta_http in PORTAS_HTTP:
            executor.submit(scan_porta_http, alvo, porta_http, timeout)

    print("Scan finalizado")

# Iniciar o codigo

scan()


