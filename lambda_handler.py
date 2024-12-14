import json
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Nome da tabela DynamoDB onde os logs serão registrados
ARN_LAMBDA_SEND_METRICS = os.getenv('ARN_LAMBDA_SEND_METRICS')
ARN_LAMBDA_SEND_BEDROCK = os.getenv('ARN_LAMBDA_SEND_BEDROCK')
HASH_KEY = os.getenv('HASH_KEY')

# --------------------------------------------------------------------
# Função Lambda que processa a requisição de autorização
# ----------------------------------------------------------------
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