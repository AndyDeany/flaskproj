import flask

from lib.user import User


app = flask.Flask(__name__)


users = [
    {
        "username": "svesar99",
        "forename": "Sara",
        "surname": "Svedlund",
        "dob": "1999/01/15",
        "bio": "The cutest kitty in all the land.",
        "quote": "Meow",
        "profile_colour": "ff21f7"
    },
    {
        "username": "andydeany",
        "forename": "Andrew",
        "surname": "Dean",
        "dob": "1998/02/26",
        "bio": "",
        "quote": "I'm a coder",
        "profile_colour": "d142f4"
    }
]

for user in users:
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
