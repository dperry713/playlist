# app/__init__.py
from flask import Flask
from app.services.database import Database
from config.config import config
import os

db = Database()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    if app.config['TESTING']:
        # Maybe use a different database for testing
        pass
        
    # Register blueprints
    from app.routes.song import bp as song_bp
    from app.routes.playlist import bp as playlist_bp
    
    app.register_blueprint(song_bp)
    app.register_blueprint(playlist_bp)
    
    return app 

from .services.database import Database
from config.config import config
    
db = Database()
    
def create_app(config_name=None):
        if config_name is None:
            config_name = os.environ.get('FLASK_CONFIG', 'default')
        
        app = Flask(__name__)
        app.config.from_object(config[config_name])
        
        # Initialize extensions
        if app.config['TESTING']:
            # Maybe use a different database for testing
            pass
            
        # Register blueprints
        from .routes.song import bp as song_bp
        from .routes.playlist import bp as playlist_bp
        
        app.register_blueprint(song_bp)
        app.register_blueprint(playlist_bp)
        
        return app