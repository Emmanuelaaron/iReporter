import datetime
        
class Incidents:
    def __init__(self):
        self.incidents = []

    def get_all_incidents(self):
        return self .incidents

    def add_incident(self, incident):
        return self.incidents.append(incident)


class Incident:
    def __init__(self, incidenceType, location, comment):
        self.incidenceType = incidenceType
        self.location = location
        self.comment = comment


    def create_incidence(self):
        return {
            "createdOn": datetime.date.today(),
            "incidenceType": self.incidenceType,
            "location": self.location,
            "status": "draft",
            "comment": self.comment,
        }