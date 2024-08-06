from flask import Blueprint, jsonify, request
from utils.database import get_connection

pessoa_bp = Blueprint('pessoa', __name__)

@pessoa_bp.route('/pessoas', methods=['GET'])
def get_pessoas():
    nome = request.args.get('nome', '')  # Obtém o parâmetro 'nome' da URL, ou uma string vazia se não fornecido

    conn = get_connection()
    cursor = conn.cursor()

    # Use o parâmetro 'nome' na consulta SQL com o placeholder correto para Firebird
    query = "SELECT CODIGOPESSOA, RAZAOSOCIAL, TELEFONE1, EMAIL FROM PESSOA WHERE RAZAOSOCIAL LIKE ?"
    cursor.execute(query, ('%' + nome + '%',))

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas)

@pessoa_bp.route('/pessoasadd', methods=['POST'])
def add_pessoa():
    data = request.json  # Obtém os dados JSON do corpo da requisição

    nome = data.get('nome', '')
    cpf = data.get('cpf', '')
    telefone = data.get('telefone', '')


    conn = get_connection()
    cursor = conn.cursor()

    # Insere os dados na tabela PESSOA (ajuste a consulta SQL conforme a estrutura do seu banco de dados)
    query = "INSERT INTO PESSOA (RAZAOSOCIAL, CPF, TELEFONE1 ) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (nome, cpf, telefone))
    conn.commit()

    conn.close()
    return jsonify({"message": "Pessoa adicionada com sucesso"}), 201