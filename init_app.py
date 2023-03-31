"""This file serves as container to create necessary instances"""
from flask import Flask
from config import FlaskConfig
from db.db_setup import db
from flask_migrate import Migrate
# ------------------------------------------------------------------------

app = Flask(__name__)

app.config.from_object(FlaskConfig())
db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)
app.app_context().push()
