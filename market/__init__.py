from enum import unique
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
#for password encryption use "bcrypt"
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__) #here we create a flask instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '778e1e6f446caf1075f0d110'
db = SQLAlchemy(app) #here we create a database instance and pass our "app" instance
bcrypt = Bcrypt(app) #for hashing passwords
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

#import from the "market" package we have created
# the "routes" file that we have created
from market import routes