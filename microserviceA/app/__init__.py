from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    from app.views.views import api_bp
    app.register_blueprint(api_bp)
    return app