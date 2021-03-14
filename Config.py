from infrastructure.context import *
import os
class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'planets.db')
    CONTEXT_FACTORY = SQLContext
    DEBUG = True
    SECRET_KEY = 'q_\xdd\x1c\xbd\x15\xeb\xdb\x8dD5\xc8\xfcR\x84\xd8?\xc5\x03rC=\x12\x98'
    SQLALCHEMY_ECHO = True
    JWT_SECRET_KEY = 'super-secret' # change this IRL
    MAIL_SERVER ='smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '2e01e613bb9a1e'
    MAIL_PASSWORD = 'e2307b0e9fc9ff'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
