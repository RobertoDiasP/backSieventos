from flask import Flask
from flask_jwt_extended import JWTManager
from routes.empresa_routes import empresa_bp
from routes.pessoa_routes import pessoa_bp
from routes.auth_routes import auth_bp
from routes.cpf_routes import cpf_bp

import config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(config.Config)
CORS(app)

# Configuração do JWT
jwt = JWTManager(app)

# Registrar Blueprints
app.register_blueprint(empresa_bp, url_prefix='/api')
app.register_blueprint(pessoa_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(cpf_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)