# config/config.py
import os
from datetime import timedelta

class Config:
    # Basic Flask config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key' # (import os) 
    from datetime import timedelta
    
    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
        DEBUG = False
        TESTING = False
        API_TITLE = 'Playlist API'
        API_VERSION = 'v1'
        RATELIMIT_DEFAULT = "200 per day;50 per hour"
        RATELIMIT_STORAGE_URL = "memory://"
        CACHE_TYPE = "SimpleCache"
        CACHE_DEFAULT_TIMEOUT = 300
        MAX_SONGS_PER_PLAYLIST = 500
        MAX_PLAYLIST_NAME_LENGTH = 100
        ALLOWED_SONG_GENRES = [
            'Rock', 'Pop', 'Jazz', 'Classical', 
            'Hip Hop', 'R&B', 'Electronic', 'Country',
            'Blues', 'Folk', 'Metal', 'Other'
        ]
        SEARCH_RESULTS_PER_PAGE = 20
        MAX_SEARCH_RESULTS = 100
        MAX_CONTENT_LENGTH = 16 * 1024 * 1024
        UPLOAD_EXTENSIONS = ['.mp3', '.wav', '.ogg']
        UPLOAD_PATH = 'uploads'
    
    class DevelopmentConfig(Config):
        DEBUG = True
        DEVELOPMENT = True
        DEBUG_TB_INTERCEPT_REDIRECTS = False
    
    class TestingConfig(Config):
        TESTING = True
        WTF_CSRF_ENABLED = False
        RATELIMIT_ENABLED = False
    
    class ProductionConfig(Config):
        DEBUG = False
        TESTING = False
        SECRET_KEY = os.environ.get('SECRET_KEY')
        RATELIMIT_DEFAULT = "1000 per day;100 per hour"
        CACHE_TYPE = "RedisCache"
        CACHE_REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
        CACHE_REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
        CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    
    config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
    }
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = False
    TESTING = False
    
    # API configs
    API_TITLE = 'Playlist API'
    API_VERSION = 'v1'
    
    # Rate limiting
    RATELIMIT_DEFAULT = "200 per day;50 per hour"
    RATELIMIT_STORAGE_URL = "memory://"
    
    # Cache configuration
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300
    
    # Playlist specific configurations
    MAX_SONGS_PER_PLAYLIST = 500
    MAX_PLAYLIST_NAME_LENGTH = 100
    ALLOWED_SONG_GENRES = [
        'Rock', 'Pop', 'Jazz', 'Classical', 
        'Hip Hop', 'R&B', 'Electronic', 'Country',
        'Blues', 'Folk', 'Metal', 'Other'
    ]
    
    # Search configurations
    SEARCH_RESULTS_PER_PAGE = 20
    MAX_SEARCH_RESULTS = 100
    
    # File upload configurations (if needed for audio files later)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_EXTENSIONS = ['.mp3', '.wav', '.ogg']
    UPLOAD_PATH = 'uploads'

class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific configurations
    DEVELOPMENT = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class TestingConfig(Config):
    TESTING = True
    # Testing-specific configurations
    WTF_CSRF_ENABLED = False
    RATELIMIT_ENABLED = False

class ProductionConfig(Config):
    # Production-specific configurations
    DEBUG = False
    TESTING = False
    
    # Use stronger secret key in production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Production rate limiting
    RATELIMIT_DEFAULT = "1000 per day;100 per hour"
    
    # Production caching
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
    CACHE_REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        
        # Production logging
        import logging
        from logging.handlers import RotatingFileHandler
        
        file_handler = RotatingFileHandler(
            'logs/playlist_api.log',
            maxBytes=10240,
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Playlist API startup')

# Dictionary to easily access different configs
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}