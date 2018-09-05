class Settings(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'q_\xdd\x1c\xbd\x15\xeb\xdb\x8dD5\xc8\xfcR\x84\xd8?\xc5\x03rC=\x12\x98'

    SQLALCHEMY_DATABASE_URI = 'postgresql://karthikravi:abc123@localhost:5432/shortner'
