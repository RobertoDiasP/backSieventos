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





#Para buscar por ano: http://127.0.0.1:5000/api/eventoBusca?eventoAno=2025
#Para buscar por código do evento: http://127.0.0.1:5000/api/eventoBusca?eventoCodigo=EVT1234
#Para buscar por ambos: http://127.0.0.1:5000/api/eventoBusca?eventoAno=2025&eventoCodigo=EVT123