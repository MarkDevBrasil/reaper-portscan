# ☠️ REAPER PORT SCAN

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Protocolos](https://img.shields.io/badge/Protocolos-TCP%20%7C%20UDP-000000?style=for-the-badge&logo=python&logoColor=white)](#recursos)
[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge)](#)
[![Tamanho do Repositório](https://img.shields.io/github/repo-size/MarkDevBrasil/REAPER_PORT_SCAN?style=for-the-badge&logo=github)](https://github.com/MarkDevBrasil/REAPER_PORT_SCAN)

Um **scanner de portas desenvolvido em Python**, utilizando a biblioteca nativa `socket` e `ThreadPoolExecutor` para executar verificações de forma concorrente.

O projeto foi criado com fins educacionais, com foco em **programação Python, redes de computadores e cibersegurança**.

---

##  Sobre o projeto

O REAPER PORT SCAN é uma ferramenta de linha de comando que verifica portas TCP e realiza sondagens básicas de portas UDP em um endereço IPv4 ou domínio informado pelo usuário.

O projeto conta com nomes de serviços predefinidos para portas comuns, configuração de tempo limite (*timeout*) e verificações adicionais de conectividade TCP nas portas HTTP e HTTPS.

##  Recursos

- **Varredura TCP:** tenta estabelecer conexões TCP para identificar portas abertas.
- **Verificação UDP:** envia datagramas UDP e verifica se há respostas.
- **Verificação HTTP/HTTPS:** realiza verificações adicionais de conectividade TCP nas portas 80 e 443.
- **Porta específica:** permite selecionar uma porta com `-p` ou `--porta`.
- **Timeout configurável:** permite ajustar o tempo de espera com `-t` ou `--timeout`.
- **Execução concorrente:** utiliza `ThreadPoolExecutor` para executar várias tarefas de verificação simultaneamente.
- **Identificação de serviços:** exibe nomes de serviços predefinidos para portas TCP conhecidas.

## Tecnologias utilizadas

- Python 3.8+
- `socket`
- `concurrent.futures`
- `argparse`

Todas as bibliotecas utilizadas pertencem à biblioteca padrão do Python. Portanto, não é necessário instalar dependências externas.

##  Instalação

Clone o repositório:

```bash
git clone https://github.com/MarkDevBrasil/REAPER_PORT_SCAN.git
cd REAPER_PORT_SCAN
```

Verifique se o Python está instalado:

```bash
python --version
```

Não é necessária a instalação de pacotes adicionais.

## 🚀 Como utilizar

### 1. Varredura padrão

Verifica todas as portas TCP e envia sondagens UDP para o mesmo intervalo:

```bash
python reaper_scan.py 127.0.0.1
```

Substitua `127.0.0.1` pelo endereço IPv4 ou domínio do sistema que você tem autorização para testar.

### 2. Verificar uma porta específica

```bash
python reaper_scan.py 127.0.0.1 -p 80
```

Na implementação atual, o programa verifica a porta selecionada tanto por TCP quanto por UDP.

### 3. Configurar o timeout

```bash
python main.py 127.0.0.1 -t 1.0
```

O valor é definido em segundos. O padrão é `0.2`.

### 4. Consultar os argumentos disponíveis

```bash
python main.py --help
```

## 🔎 Serviços predefinidos

### Portas TCP

| Porta | Serviço |
|---:|---|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 3389 | RDP |
| 5432 | PostgreSQL |

### Portas UDP

| Porta | Serviço |
|---:|---|
| 53 | DNS |
| 67 | DHCP |
| 68 | DHCP |
| 123 | NTP |
| 161 | SNMP |
| 500 | ISAKMP / IKE |
| 503 | Mapeamento personalizado |
| 1900 | SSDP |
| 5353 | mDNS |

Os nomes são associações predefinidas entre portas e serviços. Eles não confirmam qual serviço está realmente em execução no alvo.

## Como funciona

1. `socket` cria os sockets TCP e UDP.
2. `connect_ex()` tenta estabelecer uma conexão TCP.
3. As sondagens UDP enviam datagramas e aguardam respostas.
4. `ThreadPoolExecutor` executa as tarefas concorrentemente.
5. `argparse` interpreta os argumentos informados pelo usuário.

### Limitações atuais

- **UDP:** a ausência de resposta não significa necessariamente que a porta está fechada. Ela pode estar aberta, filtrada ou configurada para ignorar a sondagem.
- **HTTP/HTTPS:** o programa verifica apenas a conectividade TCP nas portas 80 e 443. Ele não realiza requisições HTTP nem analisa certificados TLS.
- **Desempenho:** a varredura de todas as portas pode gerar muitas tarefas simultâneas e demorar dependendo do alvo e do tempo limite configurado.

##  Melhorias futuras

- [ ] Melhorar a classificação dos estados das portas UDP.
- [ ] Implementar sondagens específicas para serviços UDP comuns.
- [ ] Adicionar exportação de resultados para TXT e JSON.
- [ ] Melhorar a exibição do progresso e dos resultados.
- [ ] Permitir a definição de intervalos personalizados de portas.
- [ ] Aprimorar o tratamento de erros e a resolução de domínios.
- [ ] Adicionar testes automatizados.


## Autor

**MarkDevBrasil**

[![GitHub](https://img.shields.io/badge/GitHub-MarkDevBrasil-181717?style=for-the-badge&logo=github)](https://github.com/MarkDevBrasil)

**Repositório:** [github.com/MarkDevBrasil/REAPER_PORT_SCAN](https://github.com/MarkDevBrasil/REAPER_PORT_SCAN)
