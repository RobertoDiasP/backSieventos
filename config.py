import os

class Config:
    # Configurações para JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY',
                               'aaa72b1f95adaae64a9915a4ae8ab12ca767a2935bb4620e39a91d18ae9d629f')  # Chave secreta para codificar os tokens

    # Configurações para Firebird
    FIREBIRD_HOST = 'localhost'  # Endereço IP do servidor Firebird
    FIREBIRD_PORT = 3050  # Porta padrão do Firebird
    FIREBIRD_DATABASE = 'orignallisis'  # Caminho do banco de dados
    FIREBIRD_USER = 'SYSDBA'
    FIREBIRD_PASSWORD = 'masterkey'
    FIREBIRD_CHARSET = 'ISO8859_1'
