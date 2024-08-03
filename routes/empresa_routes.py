from flask import Blueprint, request, jsonify
from utils.jwt_utils import decode_token
from utils.database import get_connection

empresa_bp = Blueprint('empresa', __name__)

@empresa_bp.route('/empresas', methods=['GET'])
def get_empresas():
    token = request.headers.get('Authorization')

    if not token or not token.startswith('Bearer '):
        return jsonify({'message': 'Token não fornecido'}), 401

    token = token.replace('Bearer ', '')
    payload = decode_token(token)

    if isinstance(payload, str):  # Se payload for uma string, então é uma mensagem de erro
        return jsonify({'message': payload}), 401

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPRESA")

    empresas = []
    for row in cursor.fetchall():
        empresa = {
            'id': row[0],
            'nome': row[1],
            # Adapte conforme os campos da sua tabela
        }
        empresas.append(empresa)

    conn.close()
    return jsonify(empresas)