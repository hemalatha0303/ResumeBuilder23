from flask import Flask
from .routes import main  # Import the blueprint
from . import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Root%40123@localhost/resume_app'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'Root@123'
    
    # Register the blueprint
    app.register_blueprint(main)
    
    return app
