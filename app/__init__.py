from flask import Flask
from config import Config
from app import classes

app = Flask(__name__)
app.config.from_object(Config)

from app import routes