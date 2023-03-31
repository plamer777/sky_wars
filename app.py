"""This unit contains a Flask instance to start the application"""
from init_app import app
from blueprints.choose_units import units_blueprint
from blueprints.main import main_blueprint
from blueprints.auth import auth_blueprint
from blueprints.new_options import options_blueprint
# ----------------------------------------------------------------------

app.register_blueprint(units_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(options_blueprint)

if __name__ == '__main__':

    app.run()
