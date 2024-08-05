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
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjcxMzM4NiwianRpIjoiNWU5OTIyMzktNjM1Yi00NDNiLTgxMjEtZmEyOWIyYTc4MjcwIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZXhhbXBsZS5jb20iLCJuYmYiOjE3MjI3MTMzODYsImNzcmYiOiJlMjI1ZTE4Yy1mYWFiLTRhNTYtYTJiNS0wZDNmOWY5NjJhNjkiLCJleHAiOjE3MjI3MTQyODZ9.0edhzvlo7EEYDELLIxy31h-BnexxvG97aBptLa2cqhY',
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjczMDI3MCwianRpIjoiOGMwNjkzOGMtMmU3Yy00ZWM5LThmMjktZGQxNDE3N2ZmZDBlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZXhhbXBsZS5jb20iLCJuYmYiOjE3MjI3MzAyNzAsImNzcmYiOiI3NTY2NTc5OS0yMjBhLTQ1ODctOWU1OS01MjkyMmQyN2YxMWQiLCJleHAiOjE3MjI3MzExNzB9.cDjfer17HIvvfhRhyNL2SzghZcZwXNbHGDQH-bgvwgo',
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyMjc5OTcxOSwianRpIjoiZjY0NWZhMzQtZWQzNi00MGFmLWFlZDAtMTJiMTE2NjI1NWI5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzZXJAZXhhbXBsZS5jb20iLCJuYmYiOjE3MjI3OTk3MTksImNzcmYiOiJmZGM3MWJhZi01YjQ0LTRjNmEtODdmMC1kMTRjZjI4N2JjNWUiLCJleHAiOjE3MjI4MDA2MTl9.lPdEjTe516HKm4j863kBXE2SnTaL53Udha7y16d7RNs'
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