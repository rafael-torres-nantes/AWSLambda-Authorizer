# 🔐 Lambda Authorization Handler

## 👨‍💻 Projeto desenvolvido por: 
[Rafael Torres Nantes](https://github.com/rafael-torres-nantes)

## Índice

* [📚 Contextualização do projeto](#-contextualização-do-projeto)
* [🛠️ Tecnologias/Ferramentas utilizadas](#%EF%B8%8F-tecnologiasferramentas-utilizadas)
* [🖥️ Funcionamento do sistema](#%EF%B8%8F-funcionamento-do-sistema)
* [🔀 Arquitetura da aplicação](#arquitetura-da-aplicação)
* [📁 Estrutura do projeto](#estrutura-do-projeto)
* [📌 Como executar o projeto](#como-executar-o-projeto)
* [🕵️ Dificuldades Encontradas](#%EF%B8%8F-dificuldades-encontradas)

## 📚 Contextualização do projeto

O __Lambda Authorization Handler__ é um repositório dedicado à documentação e compartilhamento de um script Python para autorização em AWS Lambda. Aqui, você encontrará uma explicação detalhada do código, que utiliza variáveis de ambiente e verifica tokens de autorização.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/AWS_Lambda-FF9900?logo=amazonaws&logoColor=white">](https://docs.aws.amazon.com/lambda/)
[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://docs.python.org/3/)
[<img src="https://img.shields.io/badge/dotenv-009688?logo=python&logoColor=white">](https://pypi.org/project/python-dotenv/)
[<img src="https://img.shields.io/badge/AWS_CLI-232F3E?logo=amazonaws&logoColor=white">](https://docs.aws.amazon.com/cli/)

## 🖥️ Funcionamento do sistema

O script `lambda_handler.py` realiza as seguintes operações:
1. Carrega variáveis de ambiente do arquivo `.env` usando a biblioteca `dotenv`.
2. Define os ARNs das funções Lambda a partir das variáveis de ambiente.
3. Implementa a função `lambda_handler` que:
     - Loga o evento recebido.
     - Verifica se o token de autorização é válido.
     - Constrói e retorna a resposta de autorização com base na validade do token.

```python
import json
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Nome da tabela DynamoDB onde os logs serão registrados
ARN_LAMBDA_SEND_METRICS = os.getenv('ARN_LAMBDA_SEND_METRICS')
ARN_LAMBDA_SEND_BEDROCK = os.getenv('ARN_LAMBDA_SEND_BEDROCK')
HASH_KEY = os.getenv('HASH_KEY')

def lambda_handler(event, context):
    # 1 - Log the event
    print('*********** The event is: ***************')
    print(event)
    
    # 2 - See if the person's token is valid
    auth = 'Deny'
    if event['authorizationToken'] == HASH_KEY:
        auth = 'Allow'
    
    # 3 - Construct and return the response
    authResponse = {
        "principalId": "abc123",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Resource": [
                        ARN_LAMBDA_SEND_METRICS,
                        ARN_LAMBDA_SEND_BEDROCK
                    ],
                    "Effect": auth
                }
            ]
        }
    }
    return authResponse
```

## 🔀 Arquitetura da aplicação

O sistema é baseado em uma arquitetura de microserviços, onde o backend se comunica com os serviços da AWS para análise e processamento dos tokens de autorização.

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── .env.example
├── .env
├── lambda_handler.py
└── readme.md
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rafael-torres-nantes/lambda-authorization-handler.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` baseado no `.env.example` e preencha com os valores reais.

4. **Execute a função Lambda localmente:**
   ```bash
   python lambda_handler.py
   ```

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram enfrentadas, como:

- **Configuração de variáveis de ambiente:** Garantir que todas as variáveis necessárias estejam corretamente configuradas no arquivo `.env`.
- **Validação de tokens:** Implementar uma lógica robusta para validação de tokens de autorização.
