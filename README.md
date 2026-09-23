#  Reaper Port Scan

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Socket](https://img.shields.io/badge/Socket-TCP-000000?style=for-the-badge\&logo=python\&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)](#)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/MarkDevBrasil/REAPER_PORT_SCAN?style=for-the-badge\&logo=github)](https://github.com/MarkDevBrasil/REAPER_PORT_SCAN)

Um **scanner de portas TCP simples desenvolvido em Python**, utilizando a biblioteca nativa `socket`.

>  Projeto em desenvolvimento, criado para estudos de **Python, redes e cybersecurity**.

---

##  Sobre

O Reaper Port Scan verifica portas TCP de um endereço IPv4 informado pelo usuário.

Portas atuais:

```text
21 • 22 • 80 • 443 • 3306 • 8080
```

O scanner utiliza `socket.connect_ex()` para tentar estabelecer uma conexão com cada porta.

---

##  Como Usar

```bash
git clone https://github.com/MarkDevBrasil/REAPER_PORT_SCAN.git
cd REAPER_PORT_SCAN
python3 reaper.py
```

Informe o IP:

```text
Digite o ip do alvo: 127.0.0.1
```

Exemplo:

```text
Iniciando o scan...

A porta 21: FECHADA
A porta 22: ABERTA
A porta 80: ABERTA
A porta 443: FECHADA
A porta 3306: FECHADA
A porta 8080: ABERTA
```

---
---

## ⚠️ Aviso

Utilize o scanner apenas em sistemas e redes que você possui ou tem autorização para testar.

---

## 👤 Autor

**MarkDevBrasil**

[![GitHub](https://img.shields.io/badge/GitHub-MarkDevBrasil-181717?style=for-the-badge\&logo=github)](https://github.com/MarkDevBrasil)


