class Config(object):
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_ACCESS_COOKIE_PATH = '/api/'
    JWT_REFRESH_COOKIE_PATH = '/token/refresh'
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_SECRET_KEY = 'super-secret' # Change this in real project :D!

    MAIL_SERVER = 'mail'
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = 'service@company.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False

    MONGODB_SETTINGS = {
        'db': 'weather_users',
        'host': 'db',
        'port': 27017
    }

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'debug-secret-key' # Change this in real project :D!
    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']