from flask import Flask
from lists import lists_bp

def create_app():
    app = Flask(__name__)
    app.config.update(
        ENV='development',
        FLASK_DEBUG=True,
    )
    app.register_blueprint(lists_bp)
    return app