from flask import Flask, render_template, request, redirect, send_file
from apod import fetchAPOD
from epic import fetchEPIC
from mars import fetchMARS

app = Flask(__name__)

@app.route("/")
def home():
  APOD = fetchAPOD()
  return render_template("main.html", APOD=APOD)

@app.route("/apod")
def apod():
  APOD = fetchAPOD()
  return render_template("apod.html", APOD=APOD)

@app.route("/epic")
def epicPage():
  EPIC = fetchEPIC()
  return render_template("epic.html", EPIC=EPIC)

@app.route("/mars")
def mars():
  MARS = fetchMARS()
  return render_template("mars.html", MARS=MARS)

app.run()