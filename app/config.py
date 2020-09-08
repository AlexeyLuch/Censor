class Configuration(object):
    CSRF_ENABLED = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/censor'
    SECRET_KEY = "OMG_PASSWORD"

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    UPLOADS_DEFAULT_DEST = 'static/images'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


