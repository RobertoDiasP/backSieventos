# utils/jwt_utils.py
import jwt
import datetime
from config import Config

def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)  # Ajuste o tempo de expiração conforme necessário
    }
    return jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm='HS256')


def decode_token(token):
    # Lista de tokens válidos (exemplo, você pode usar um banco de dados ou cache na prática)
    valid_tokens = [
        
    ]

    try:
        # Decodifica o token
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=['HS256'])

        # Verifica se o token está na lista de tokens válidos
        if token not in valid_tokens:
           return 'Token não válido'

        return payload  # Retorna o payload se o token for válido e estiver na lista

    except jwt.ExpiredSignatureError:
        return 'Token expirado'
    except jwt.InvalidTokenError:
        return 'Token inválido'