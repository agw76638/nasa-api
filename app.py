from flask import Flask, render_template, request, redirect, send_file
from nasa import fetchAPOD
from epic import fetchEPIC

app = Flask(__name__)

@app.route("/")
def home():
  APOD = fetchAPOD()
  return render_template("main.html", APOD=APOD)

@app.route("/epic")
def epicPage():
  EPIC = fetchEPIC()
  return render_template("epic.html", EPIC=EPIC)

app.run()