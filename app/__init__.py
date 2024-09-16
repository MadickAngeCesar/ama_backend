from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

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
    CORS(app)  # Allow all origins

    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
    
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.main)
        db.create_all()

    return app
