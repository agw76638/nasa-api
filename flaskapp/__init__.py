from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flaskapp.apod import fetchAPOD
from flaskapp.epic import fetchEPIC
from flaskapp.mars import getMars

app = Flask(__name__)
app.config["SECRET_KEY"] = "9a67ced28bf30addbc21e2fe231206dd"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from flaskapp import routes
