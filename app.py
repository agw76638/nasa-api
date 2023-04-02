from datetime import datetime
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_file,
    flash,
    redirect,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from apod import fetchAPOD
from epic import fetchEPIC
from mars import getMars

app = Flask(__name__)
app.config["SECRET_KEY"] = "9a67ced28bf30addbc21e2fe231206dd"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.Relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}',)"


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


app.run()
