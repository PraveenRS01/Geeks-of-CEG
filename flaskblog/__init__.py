import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SECRET_KEY"] = "63dfa4322c5d6f9ec07df214c1088089"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "praveenrs0111@gmail.com"
app.config["MAIL_PASSWORD"] = "indc8311"
mail = Mail(app)

from flaskblog.errors.handlers import errors

app.register_blueprint(errors)

from flaskblog import routes
