import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = '5_&bx(zt%))kke4a)imn@kb8)oi6$4ng'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(BASE_DIR, 'application.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
