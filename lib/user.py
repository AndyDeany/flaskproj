import datetime
import re


class User(object):
    """Class for users on the webapp"""
    # Class methods and attributes
    users = []

    @classmethod
    def find(cls, username):
        return next((u for u in cls.users if u.username == username), None)

    def __init__(self,
                 username,
                 password,
                 forename,
                 surname,
                 dob,   # Should be a string YYYY/MM/DD
                 bio="Bio not found.",
                 quote="No quote found.",
                 profile_colour="478dff"):
        self.username = username
        self.password = password
        self.set_name(forename, surname)
        self.set_dob(dob)
        self.bio = bio
        self.quote = quote

        self.profile_colour = profile_colour

        self.users.append(self)

    def set_name(self, forename=None, surname=None):
        if forename is None:
            forename = self.forname
        if surname is None:
            surname = self.surname
        self.forename = forename.capitalize()
        self.surname = surname.capitalize()
        self.fullname = self.forename + " " + self.surname

    def set_dob(self, dob_string):
        """Set dob to a datetime.date object dependent on the given string"""
        self.dob = datetime.date(*map(int, re.split(r"[-/ \.]", dob_string)))
