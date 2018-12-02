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
        list_ = Users()
        return {
            # "user_id": len(list_.get_all_users()) + 1,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email": self.email,
            "password": self.password,
            "username": self.username,
            "registered": datetime.date.today()
        }
        




# class Incidents:
#     def __init__(self, incidenceType, location, comment):
#         self.incidenceType = incidenceType
#         self.location = location
#         self.comment = comment

#     @staticmethod
#     def get_all_incidents():
#         return incidents

#     def create_incidence(self, user_id):
#         for user in users:
#             if user["user_id"] == user_id:
#                 incident = {
#                     "flag_id": len(incidents) + 1,
#                     "createdOn": datetime.date.today(),
#                     "incidenceType": self.incidenceType,
#                     "location": self.location,
#                     "status": "draft",
#                     "comment": self.comment,
#                     "createdby": user_id
#                 }
#                 incidents.append(incident)
#             return incident