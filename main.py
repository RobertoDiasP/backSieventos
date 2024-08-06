from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Importação dos Blueprints
from routes.empresa_routes import empresa_bp
from routes.pessoaCad_routes import cadastro_bp
from routes.pessoa_routes import pessoa_bp
from routes.auth_routes import auth_bp
from routes.cpf_routes import cpf_bp

import config

app = Flask(__name__)
app.config.from_object(config.Config)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

# Configuração do JWT
jwt = JWTManager(app)

# Registrar Blueprints com prefixos
app.register_blueprint(empresa_bp, url_prefix='/api/')
app.register_blueprint(pessoa_bp, url_prefix='/api/')
app.register_blueprint(auth_bp, url_prefix='/api/')
app.register_blueprint(cpf_bp, url_prefix='/api/')
app.register_blueprint(cadastro_bp, url_prefix='/api/')  # Prefixo para cadastro_bp

if __name__ == '__main__':
    app.run(debug=True)
