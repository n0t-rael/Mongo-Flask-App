from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import config

app = Flask(__name__)
app.config["MONGO_URI"] = config.MONGO_URI
app.secret_key = config.SECRET_KEY

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

from routes.auth import auth_bp
from routes.blog import blog_bp
app.register_blueprint(auth_bp)
app.register_blueprint(blog_bp)

if __name__ == "__main__":
    app.run(debug=True)
