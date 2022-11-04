from flask import Flask, render_template, request, redirect, send_file
from nasa import fetchAPOD

app = Flask(__name__)

@app.route("/")
def home():
  APOD = fetchAPOD()
  return render_template("main.html", APOD=APOD)
  #return "hello"

app.run()