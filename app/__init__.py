from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        app.config.from_mapping(
            SECRET_KEY='dev',
            SQLALCHEMY_DATABASE_URI='sqlite:///routine.db',
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.main)
        db.create_all()

    return app
