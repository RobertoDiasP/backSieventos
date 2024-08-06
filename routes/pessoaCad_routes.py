from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
from utils.database import get_connection

# Novo nome do Blueprint
cadastro_bp = Blueprint('cadastro', __name__)

@cadastro_bp.route('/pessoasCadastro', methods=['POST'])
def add_pessoa():
    data = request.get_json()
    razaosocial = data.get('RAZAOSOCIAL')
    status = data.get('STATUS')
    telefone1 = data.get('TELEFONE1')
    cpf = data.get('CPF')

    conn = get_connection()
    cursor = conn.cursor()

    # Corrigido: número de valores deve corresponder ao número de colunas
    query = "INSERT INTO PESSOA (RAZAOSOCIAL, STATUS, TELEFONE1, CPF) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (razaosocial, status, telefone1,cpf))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Pessoa adicionada com sucesso!'}), 201

# Configuração da aplicação Flask
app = Flask(__name__)
CORS(app)

# Registrar Blueprint com o novo nome
app.register_blueprint(cadastro_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
