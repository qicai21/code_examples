from flask import Flask, render_template
from lists import lists_bp
import secrets
from flask_wtf.csrf import CSRFProtect, CSRFError

def create_app():
    app = Flask(__name__)
    app.config.update(
        ENV='development',
        FLASK_DEBUG=True,
        SECRET_KEY=secrets.token_hex(16)
    )
    app.register_blueprint(lists_bp)
    CSRFProtect(app)

    @app.errorhandler(CSRFError)
    def csrf_error(e):
        return render_template('csrf_error.html', reason=e.description), 403

    return app

