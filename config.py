import os

class Config(object):
    """
    Common configurations
    """
    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SECRET_KEY = "SECRET"

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = "SECRET"

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
    SECRET_KEY = "SECRET"

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
