from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# I import the routes and classes at the bottom of the script because these modules needs to import the app variable defined in this script
from app import classes
from app import routes