from flask import Flask
from config import FlaskConfig
from db.db_setup import db
# ------------------------------------------------------------------------

app = Flask(__name__)
app.config.from_object(FlaskConfig())
db.init_app(app)
app.app_context().push()
