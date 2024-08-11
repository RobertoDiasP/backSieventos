# routes/auth_routes.py

from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from utils.database import get_connection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email or not password:
        return jsonify({"msg": "Missing email or password"}), 400

    # Obter conexão com o banco de dados
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Consultar o banco de dados para obter a senha armazenada
        cursor.execute("SELECT senha_web FROM usuario WHERE email = ?", (email,))
        stored_password = cursor.fetchone()

        if stored_password and stored_password[0] == password:
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"msg": "Database error", "error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
