from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os
from backend.settings.base import BACKEND_DIR, FRONTEND_DIR

db = SQLAlchemy()
mail = Mail()


def create_app(test_config=None, debug: bool = False):
    app = Flask(
        "Small Business E-Commerce",
        template_folder=os.path.join(FRONTEND_DIR, "templates"),
        static_folder=os.path.join(FRONTEND_DIR, "static"),
    )

    if test_config is None and debug is False:
        app.config.from_pyfile(
            os.path.join(BACKEND_DIR, "settings", "prod.py"), silent=True
        )
    if test_config is None and debug is True:
        app.config.from_pyfile(
            os.path.join(BACKEND_DIR, "settings", "dev.py"), silent=False
        )
    else:
        app.config.from_mapping(test_config)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["MYSQL_DATABASE_CHARSET"] = "utf8mb4"
    secret_key = os.urandom(32)
    app.config["SECRET_KEY"] = secret_key

    with app.app_context() as f:
        f.push()
        db.init_app(app)
        mail.init_app(app)

        return app


flask_app = create_app(debug=True)
