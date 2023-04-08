from flask import (
    render_template,
    request,
    redirect,
    send_file,
    flash,
    redirect,
    url_for,
)
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "green lighten-4")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been loged in!", "green lighten-4")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful", "red lighten-4")
    return render_template("login.html", title="Login", form=form)


@app.route("/apod")
def apod():
    APOD = fetchAPOD()
    return render_template("apod.html", APOD=APOD, title="APOD")


@app.route("/epic")
def epicPage():
    EPIC = fetchEPIC()
    return render_template("epic.html", EPIC=EPIC, title="EPIC")


@app.route("/mars")
def mars():
    MARS = getMars()
    return render_template("mars.html", MARS=MARS, title="Mars Photo")
