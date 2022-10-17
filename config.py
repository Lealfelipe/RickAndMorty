import os


class Config(object):
    TESTING = False
    DEBUG = False


class ProductionConfig(Config):
    DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class DevelopmentConfig(Config):
    DATABASE_URI = "sql:///:memory:"
    TESTING = DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
