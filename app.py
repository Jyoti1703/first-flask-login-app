from flask import Flask, request, url_for, redirect, Response, session

app = Flask(__name__)
app.secret_key = "SuperSecretKey"


# Home page logic
@app.route("/", methods=["POST", "GET"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "password":

            session["username"] = username

            return redirect(url_for("welcome"))

        else:

            return Response(
                "Invalid credentials, try again.",
                mimetype="text/plain"
            )

    return '''

<!DOCTYPE html>

<html>

<head>

    <title>Login Page</title>

    <style>

        body {

            background-color: #f2f2f2;
            font-family: Arial;
        }

        .container {

            width: 300px;

            margin: 100px auto;

            padding: 30px;

            background-color: white;

            border-radius: 10px;

            box-shadow: 0px 0px 10px gray;

            text-align: center;
        }

        input {

            width: 90%;

            padding: 10px;

            margin: 10px 0;
        }

        button {

            padding: 10px 20px;

            background-color: #007bff;

            color: white;

            border: none;

            border-radius: 5px;

            cursor: pointer;
        }

        button:hover {

            background-color: #0056b3;
        }

    </style>

</head>

<body>

    <div class="container">

        <h2>Login Page</h2>

        <form method="post">

            <input
                type="text"
                name="username"
                placeholder="Enter Username"
                required>

            <input
                type="password"
                name="password"
                placeholder="Enter Password"
                required>

            <br>

            <button type="submit">
                Login
            </button>

        </form>

    </div>

</body>

</html>

'''


# Welcome page logic
@app.route("/welcome")
def welcome():

    if "username" in session:

        return f'''

        <h1>
            Welcome, {session['username']}!
        </h1>

        <a href="{url_for('logout')}">
            Logout
        </a>

        '''

    else:

        return redirect(url_for("login"))


# Logout page logic
@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect(url_for("login"))


if __name__ == "__main__":

    app.run(debug=True)