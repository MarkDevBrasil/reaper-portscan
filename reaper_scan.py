# prototype
# Reaper Port Scan
# In dev


import socket


def scan():
    alvo = input("Digite o ip do alvo: ")
    portas = [21, 22, 80, 443, 3306, 8080]

    print("Iniciando o scan...")

    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1)

        resultado = s.connect_ex((alvo, porta))

        if resultado == 0:
            print(f"A porta {porta}: ABERTA")
        else:
            print(f"a porta {porta}: FECHADA")

        s.close()

scan()
