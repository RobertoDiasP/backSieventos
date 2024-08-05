from flask import Blueprint, jsonify, request
from utils.database import get_connection

cpf_bp = Blueprint('cpf', __name__)

@cpf_bp.route('/cpf', methods=['GET'])
def get_cpf():
    cpf = request.args.get('cpf', '')  # Obtém o parâmetro 'cpf' da URL, ou uma string vazia se não fornecido

    conn = get_connection()
    cursor = conn.cursor()

    # Use o parâmetro 'cpf' na consulta SQL
    query = "SELECT * FROM PESSOA WHERE CPF = ?"
    cursor.execute(query, (cpf,))  # O CPF é comparado exatamente

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas)
