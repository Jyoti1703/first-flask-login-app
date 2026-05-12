from flask import Flask, url_for
from flask import redirect, session
from flask import render_template, flash

from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Length
)

app = Flask(__name__)

app.secret_key = "SuperSecretKey"


# WTForms Login Form
class LoginForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(
                min=6,
                message="Password must be at least 6 characters"
            )
        ]
    )

    submit = SubmitField("Login")


# Multiple Users
users = {

    "admin": "password",

    "jerry": "123456",

    "john": "abcdef",

    "alice": "alice123"
}


# Login Page
@app.route("/", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        username = form.username.data

        password = form.password.data

        if username in users and users[username] == password:

            session["username"] = username

            flash("Login successful!", "success")

            return redirect(url_for("welcome"))

        else:

            flash("Invalid username or password", "error")

            return redirect(url_for("login"))

    return render_template(
        "login.html",
        form=form
    )


# Welcome Page
@app.route("/welcome")
def welcome():

    if "username" in session:

        return render_template(
            "welcome.html",
            username=session["username"]
        )

    else:

        flash("Please login first", "warning")

        return redirect(url_for("login"))


# Logout
@app.route("/logout")
def logout():

    session.pop("username", None)

    flash("Logged out successfully", "success")

    return redirect(url_for("login"))


if __name__ == "__main__":

    app.run(debug=True)