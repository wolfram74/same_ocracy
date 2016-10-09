from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

db = SQLAlchemy(app)

app.config.from_object(os.environ['APP_SETTINGS'])

from project.home.views import home_blueprint



app.register_blueprint(home_blueprint)
