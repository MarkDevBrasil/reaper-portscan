# ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗
# ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
# ██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
# ██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
# ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
# ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
# REAPER PORT SCANNER
# Made By MarkDevBrasil
# My GitHub: https://github.com/MarkDevBrasil

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



import socket
from concurrent.futures import ThreadPoolExecutor

# Função para escanear uma porta específica em um alvo
def scan_porta(alvo, porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.2)

        resultado = s.connect_ex((alvo, porta))

    if resultado == 0:
        serviço = SERVICOS.get(porta, "Desconhecido")
        print(f"[+] Porta {porta}/tcp OPEN - Serviço: {serviço}")

# Função para realizar o scan de portas em um alvo específico
def scan():
    alvo = input("Digite o IP do alvo: ")

    portas = range(1, 65536)

    print("Iniciando o scan...")
# With
    with ThreadPoolExecutor(max_workers=100) as executor:
        for porta in portas:
            executor.submit(scan_porta, alvo, porta)

    print("Scan finalizado.")

# Iniciar o codigo
scan()
