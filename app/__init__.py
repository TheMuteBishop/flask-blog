from flask import Flask

def create_app(extra_config_settings={}):
    """Create a Flask application.
    """
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello from Flask!'

    return app