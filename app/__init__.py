import os
from flask import Flask
from dotenv import load_dotenv
from .routes.pet_routes import bp as pets_bp
from .db import db, migrate
from .models import pet

# Load environment variables from .env file
load_dotenv()

def create_app(config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(pets_bp)

    return app