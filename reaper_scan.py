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


# Bibliotecas
import socket
from concurrent.futures import ThreadPoolExecutor
import argparse

# Função para escanear uma porta específica em um alvo
def scan_porta(alvo, porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.2)

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

args = parser.parse_args()

# Função para informar os dados de um alvo para realizar o scan
def scan():
    alvo = args.alvo

    portas = range(1, 65536)

    print("Iniciando o scan")
# Informa o limite maximo e threads para o scan de uma porta.
    with ThreadPoolExecutor(max_workers=100) as executor:
        for porta in portas:
            executor.submit(scan_porta, alvo, porta)

    print("Scan finalizado")

# Iniciar o codigo



scan()
