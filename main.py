import json

import flask

from lib.user import User


app = flask.Flask(__name__)

with open("assets/users.json") as users_json:
    for user in json.load(users_json):
        User(**user)


@app.route("/user/<username>")
@app.route("/u/<username>")
def profile(username):
    user = User.find(username)
    if user is None:
        return "User '%s' not found." % username
    else:
        return flask.render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
