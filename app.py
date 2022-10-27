import secrets
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect, CSRFError
from mongoengine import connect
from lists import lists_bp


def create_app():
    app = Flask(__name__)
    app.config.update(
        ENV='development',
        FLASK_DEBUG=True,
        SECRET_KEY=secrets.token_hex(16),
    )
    app.register_blueprint(lists_bp)
    CSRFProtect(app)
    connect(
        db='superlists',
        host='localhost',
        port=27017,
        username='qicai21', 
        password='5233',
        authentication_source='admin',
        uuidRepresentation="pythonLegacy"
    )

    @app.errorhandler(CSRFError)
    def csrf_error(e):
        return render_template('csrf_error.html', reason=e.description), 403
    return app