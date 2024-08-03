from flask import Flask
from flask_jwt_extended import JWTManager
from routes.empresa_routes import empresa_bp
from routes.pessoa_routes import pessoa_bp
from routes.auth_routes import auth_bp
import config

app = Flask(__name__)
app.config.from_object(config.Config)

# Configuração do JWT
jwt = JWTManager(app)

# Registrar Blueprints
app.register_blueprint(empresa_bp, url_prefix='/api')
app.register_blueprint(pessoa_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)