from flask import Blueprint, jsonify
from utils.database import get_connection

pessoa_bp = Blueprint('pessoa', __name__)


@pessoa_bp.route('/pessoas', methods=['GET'])
def get_pessoas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPRESA")

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas)
