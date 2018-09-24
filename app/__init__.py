from flask import Flask

# content here

app = Flask(__name__)

# blueprints here

from app.main import bp as main_bp
from app.auth import bp as auth_bp

app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(auth_bp, url_prefix="/auth")
