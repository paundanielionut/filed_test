import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_URI = os.path.join(ROOT_DIR, os.environ.get('DATABASE_URI'))

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    pass
