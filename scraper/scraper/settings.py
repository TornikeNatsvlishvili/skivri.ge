import os

class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('APP_SECRET', 'CHANGE')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'CHANGE')
    MYSQL_PORT = os.environ.get('MYSQL_PORT', 'CHANGE')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'CHANGE')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'CHANGE')
    MYSQL_PASS = os.environ.get('MYSQL_PASS', 'CHANGE')    
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    FETCH_WAIT_SECONDS = 60 * 15  # 15 minutes

class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True