from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
from utils.database import get_connection
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

@pessoa_bp.route('/pessoaId', methods=['GET'])
def get_pessoa_by_id():
    id = request.args.get('id', '')  # Obtém o parâmetro 'id' da URL, ou uma string vazia se não fornecido

    conn = get_connection()
    cursor = conn.cursor()

    # Use o parâmetro 'id' na consulta SQL com o placeholder correto para Firebird
    query = "SELECT * FROM vw_pessoa WHERE codigopessoa = ?"

    cursor.execute(query, (id,))

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas, id)

@pessoa_bp.route('/pessoaFinId', methods=['GET'])
def get_pessoa_fin_by_id():
    id = request.args.get('id', '')  # Obtém o parâmetro 'id' da URL, ou uma string vazia se não fornecido
    aberto_quitado = request.args.get('aberto_quitado','')  # Obtém o parâmetro 'aberto_quitado' da URL,

    conn = get_connection()
    cursor = conn.cursor()

    # Use o parâmetro 'id' na consulta SQL com o placeholder correto para Firebird
    query = "SELECT * FROM vw_contareceber WHERE ABERTO_QUITADO = ? and codigopessoa = ?"

    cursor.execute(query, (aberto_quitado, id,))

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas, id)
