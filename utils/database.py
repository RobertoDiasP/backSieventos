import firebirdsql
from config import Config

def get_connection():
    return firebirdsql.connect(
        host='localhost',
        database=Config.FIREBIRD_DATABASE,
        user=Config.FIREBIRD_USER,
        password=Config.FIREBIRD_PASSWORD,
        charset=Config.FIREBIRD_CHARSET
    )
