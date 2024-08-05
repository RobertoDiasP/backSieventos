from flask import Blueprint, jsonify, request
from utils.database import get_connection

pessoa_bp = Blueprint('pessoa', __name__)

@pessoa_bp.route('/pessoas', methods=['GET'])
def get_pessoas():
    nome = request.args.get('nome', '')  # Obtém o parâmetro 'nome' da URL, ou uma string vazia se não fornecido

    conn = get_connection()
    cursor = conn.cursor()

    # Use o parâmetro 'nome' na consulta SQL com o placeholder correto para Firebird
    query = "SELECT * FROM PESSOA WHERE RAZAOSOCIAL LIKE ?"
    cursor.execute(query, ('%' + nome + '%',))

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas)
