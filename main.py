import json

from flask import Flask, render_template, redirect, url_for, request

from lib.user import User


app = Flask(__name__)

with open("assets/users.json") as users_json:
    for user in json.load(users_json):
        User(**user)


@app.route("/")
def index():
    return "Hello, World!"

@app.route("/login", methods=("GET", "POST"))
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        user = User.find(username)
        if user is None:
            error = "User not found. Please try again."
        elif request.form["password"] == user.password:     # Valid login
            return redirect(url_for("profile", username=username))
        else:
            error = "Invalid password. Please try again."
    return render_template("login.html", error=error)

@app.route("/user/<username>")
@app.route("/u/<username>")
def profile(username):
    user = User.find(username)
    if user is None:
        return f"User '{username}' not found."
    else:
        return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
