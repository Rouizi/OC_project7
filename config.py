import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# .env contains the SECRET_KEY and the GOOGLE_MAP_KEY
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    GOOGLE_MAP_KEY = os.environ.get('GOOGLE_MAP_KEY')