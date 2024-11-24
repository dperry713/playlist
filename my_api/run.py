# run.py
from flask import Flask
from config.config import config

# Create the Flask application
app = Flask(__name__)

# Determine the configuration to use
# You can replace 'development' with 'production' or 'testing' as needed
config_name = 'development'
app.config.from_object(config[config_name])

# Initialize any extensions here (if required)
# e.g., initialize database, cache, etc.

@app.route('/')
def index():
    return "Welcome to Playlist API!"

if __name__ == '__main__':
    app.run()
from flask import Flask
from config.config import config
from app import create_app

app = create_app(config_name='development')

if __name__ == '__main__':
    app.run()