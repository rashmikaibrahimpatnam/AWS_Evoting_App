from collections import namedtuple


class UserDetails:
    def __init__(self, first_name, last_name, password, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.phone = phone
        self.email = email
        self.verified = "N"

    def print(self):
        print(self.first_name + " " + self.last_name + " " +
              self.password + " " + self.phone + " " + self.email)

    def decode(user_dictionary):
        return namedtuple('X', user_dictionary.keys())(*user_dictionary.values())