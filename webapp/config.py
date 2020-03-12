from datetime import timedelta
import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False

SECRET_KEY = os.environ.get('SECRET_KEY') or 'vui1pirae9vah7ReisheiThohloo7K25'

REMEMBER_COOKIE_DURATION = timedelta(days=int(os.environ.get('REMEMBER_COOKIE_DURATION') or 5))
