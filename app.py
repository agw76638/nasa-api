from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from apod import fetchAPOD
from epic import fetchEPIC
from mars import getMars

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/apod")
def apod():
  APOD = fetchAPOD()
  return render_template("apod.html", APOD=APOD, title='APOD')

@app.route("/epic")
def epicPage():
  EPIC = fetchEPIC()
  return render_template("epic.html", EPIC=EPIC, title='EPIC')

@app.route("/mars")
def mars():
  MARS = getMars()
  return render_template("mars.html", MARS=MARS, title='Mars Photo')

app.run()