import datetime

class Users:
    def __init__(self):
        self.users = []

    def get_all_users(self):
        return self.users 

    def add_user(self, user):
        return self.users.append(user)

class User:
    def __init__(self, firstname, lastname, othernames, email, password, username):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.password = password
        self.username = username
    
    def signup(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email": self.email,
            "password": self.password,
            "username": self.username,
            "registered": datetime.date.today()
        }
        

