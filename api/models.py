import datetime

users = [
    {
        "id": 1,
        "firstname": "Emmanuel",
        "lastname": "Aaron",
        "othernames": "isabirye",
        "email": "emmanuelisabirye9@gmail.com",
        "username": "sonibil",
        "registered": 2018-11-16,
    }
]

incidents = [
    {
        "id": 1,
        "createdOn": 2018-10-17,
        "incidenceType": "red flag",
        "location": "7652, 67656",
        "status": "resolved",
        "comment": "corruption at icc"
    }
]


class Users:
    def __init__(self, firstname, lastname, othernames, email, password, username):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.password = password
        self.username = username
    
    def signup(self):
        user = {
            "id": len(users) + 1,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email": self.email,
            "username": self.username,
            "registered": datetime.date.today()
        }
        users.append(user)

class Incidents:
    def __init__(self, incidenceType, location, comment):
        self.incidenceType = incidenceType
        self.location = location
        self.comment = comment

    @staticmethod
    def get_all_incidents():
        return incidents

    def create_incidence(self, id):
        for user in users:
            if user["id"] == id:
                incident = {
                    "id": len(incidents) + 1,
                    "createdOn": datetime.date.today(),
                    "incidenceType": self.incidenceType,
                    "location": self.location,
                    "status": "draft",
                    "comment": self.comment
                }
                incidents.append(incident)
                return incident