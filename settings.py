import os

SHORT_ID_REGEX = r'^[a-zA-Z0-9]{1,16}$'
SHORT_ID_LENGTH = 6
SHORT_ID_MAX_LENGTH = 16


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        default='sqlite:///db.sqlite3',
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET KEY')
