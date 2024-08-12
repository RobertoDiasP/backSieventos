from flask import Blueprint, jsonify, request
from utils.database import get_connection
from datetime import time

agenda_bp = Blueprint('agenda', __name__)

@agenda_bp.route('/agenda', methods=['GET'])
def get_pessoas():
    dataI = request.args.get('dataInicio', '')  # Obtém o parâmetro 'dataInicio' da URL
    dataF = request.args.get('dataFim', '')  # Obtém o parâmetro 'dataFim' da URL

    conn = get_connection()
    cursor = conn.cursor()

    # Use o parâmetro 'dataInicio' e 'dataFim' na consulta SQL com o placeholder correto para Firebird
    query = "SELECT * FROM agendaevento WHERE data BETWEEN ? AND ?"
    cursor.execute(query, (dataI, dataF))

    # Obtenha os nomes das colunas
    columns = [desc[0] for desc in cursor.description]

    pessoas = []
    for row in cursor.fetchall():
        pessoa = dict(zip(columns, row))
        # Converta os campos do tipo `time` para strings
        for key, value in pessoa.items():
            if isinstance(value, time):
                pessoa[key] = value.strftime('%H:%M:%S')  # Formata o objeto `time` como string
        pessoas.append(pessoa)

    conn.close()
    return jsonify(pessoas)
