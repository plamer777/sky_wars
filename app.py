"""This unit contains a Flask instance to start the application"""
from flask import Flask
from blueprints.choose_units import units_blueprint
from blueprints.main import main_blueprint
# ----------------------------------------------------------------------
app = Flask(__name__)
app.register_blueprint(units_blueprint)
app.register_blueprint(main_blueprint)

if __name__ == '__main__':

    app.run()
