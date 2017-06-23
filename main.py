import flask

from lib.user import User


app = flask.Flask(__name__)


User(username="svesar99",
     forename="sara", surname="svedlund",
     dob=(1999, 1, 15),
     bio="The cutest kitty in all the land.",
     quote="Meow",
     profile_colour="ff21f7")


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
