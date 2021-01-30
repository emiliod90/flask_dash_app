__version__ = '0.1.0'

"""Initialize Flask app."""
from flask import Flask


def init_app():
    """Construct core Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # import dash application
        from .plotlydash.dashboard1 import init_dashboard
        app = init_dashboard(app)

        return app
