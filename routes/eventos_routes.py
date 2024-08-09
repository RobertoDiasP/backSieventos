from flask import Blueprint, jsonify, request
from utils.database import get_connection

evento_bp = Blueprint('ano_codigo', __name__)


@evento_bp.route('/eventoBusca', methods=['GET'])
def get_evento_by_ano_codigo():
    evento_ano_param = request.args.get('eventoAno', '').strip()
    evento_codigo_param = request.args.get('eventoCodigo', '').strip()

    # Inicializa a consulta SQL
    query = "SELECT * FROM vw_evento WHERE 1=1"
    params = []

    # Adiciona a condição para o ano, se fornecido
    if evento_ano_param.isdigit():
        query += " AND ANOEVENTO = ?"
        params.append(int(evento_ano_param))

    # Adiciona a condição para o código do evento, se fornecido
    if evento_codigo_param:
        query += " AND CODIGOEVENTO = ?"
        params.append(evento_codigo_param)

    # Verifica se pelo menos um parâmetro foi fornecido
    if not params:
        return jsonify({"error": "Pelo menos um parâmetro ('eventoAno' ou 'eventoCodigo') deve ser fornecido."}), 400

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, tuple(params))  # Executa a consulta com os parâmetros

    columns = [desc[0] for desc in cursor.description]

    eventos = []
    for row in cursor.fetchall():
        evento = dict(zip(columns, row))
        eventos.append(evento)

    conn.close()
    return jsonify(eventos)

@evento_bp.route('/eventoPessoa', methods=['GET'])
def get_pessoa_evento():
    evento_pessoa = request.args.get('codigoevento', '').strip()

    # Inicializa a consulta SQL
    query = "SELECT * FROM vw_pessoaevento WHERE codigoevento = ?"
    params = []


    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, (evento_pessoa,)) # Executa a consulta com os parâmetros

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas)

@evento_bp.route('/eventoFin', methods=['GET'])
def get_evento_fin():
    evento_fin = request.args.get('codigoevento', '').strip()

    # Inicializa a consulta SQL
    query = "SELECT * FROM vw_contareceber WHERE codigoevento = ?"
    params = []


    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, (evento_fin,)) # Executa a consulta com os parâmetros

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas)




#Para buscar por ano: http://127.0.0.1:5000/api/eventoBusca?eventoAno=2025
#Para buscar por código do evento: http://127.0.0.1:5000/api/eventoBusca?eventoCodigo=EVT1234
#Para buscar por ambos: http://127.0.0.1:5000/api/eventoBusca?eventoAno=2025&eventoCodigo=EVT123