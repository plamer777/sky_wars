from init_app import app
from services.auth_service import AuthService
from utils import load_from_json
# -------------------------------------------------------------------------


admin_data = load_from_json('admin.json')
with app.app_context():
    AuthService().register_user(admin_data)
