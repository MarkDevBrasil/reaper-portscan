# ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗
# ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
# ██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
# ██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
# ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
# ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
# REAPER PORT SCANNER
# Made By MarkDevBrasil
# My GitHub: https://github.com/MarkDevBrasil

import socket
from concurrent.futures import ThreadPoolExecutor

# Função para escanear uma porta específica em um alvo
def scan_porta(alvo, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)

    resultado = s.connect_ex((alvo, porta))

    if resultado == 0:
        print(f"[+] Porta {porta}: ABERTA")
    s.close()

# Função para realizar o scan de portas em um alvo específico
def scan():
    alvo = input("Digite o IP do alvo: ")

    portas = range(1, 65536)

    print("Iniciando o scan...")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for porta in portas:
            executor.submit(scan_porta, alvo, porta)

    print("Scan finalizado.")


scan()
