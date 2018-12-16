import unittest
# from api import*
from api import app
from flask import json
import datetime
# from api.models import Users

class TestUser(unittest.TestCase):

    def Setup(self):
        self.tester = app.test_client(self)

    def test_signupuser(self):

        user = dict(
            firstname="Donald",
            lastname="ngiya",
            othernames="Danny",
            email="ngiya@gams.com",
            password="ghgdhgd",
            username="dojo"
        )
        resp = app.test_client(self).post(
            "api/v1/signup", 
            content_type="application/json",
            data=json.dumps(user)
        )

        reply = json.loads(resp.data.decode())

        self.assertTrue(reply)
        self.assertEqual(reply["message"], "You've signed up sucessfully!")
        self.assertIn("You've signed up sucessfully!", str(reply))
        self.assertEqual(reply["data"]['email'], 'ngiya@gams.com')
        self.assertEqual(reply["data"]["lastname"], "ngiya")
        self.assertEqual(reply["data"]["username"], "dojo")
        self.assertEqual(reply["data"]["firstname"], "Donald")
        self.assertEqual(resp.status_code, 201)

    def test_signupuser_without_a_field(self):
        user = dict(
            firstname="",
            lastname="ngiya",
            othernames="Danny",
            email="ngiya@gams.com",
            password="ghgdhgd",
            username="dojo"
        )
        resp = app.test_client(self).post(
            "api/v1/signup",
            content_type="application/json",
            data = json.dumps(user)
        )

        reply = json.loads(resp.data.decode())

        self.assertEqual(reply["message"], "All fields must be filled!")
        self.assertEqual(resp.status_code, 400)
        
    
class TestFlags(unittest.TestCase):
    
    def SetUp(self):
        self.tester = app.test_client(self)

    def test_create_red_flag(self):
        user = dict(
            firstname="itui",
            lastname="isa",
            othernames="Danny",
            email="ngiya@gam.com",
            password="ghgdhgd",
            username="emma"
        )
        resp = app.test_client(self).post(
            "api/v1/signup", 
            content_type="application/json",
            data=json.dumps(user)
        )

        reply = json.loads(resp.data.decode())

        self.assertIn("You've signed up sucessfully!", str(reply))
        self.assertEqual(resp.status_code, 201)

        incident = dict(
        incidenceType = "Red flag",
        location = "752, 67056",
        comment = "corruption at icc",
        user_id = 1

        )
        resp = app.test_client(self).post(
            "api/v1/red-flags",
            content_type="application/json",
            data=json.dumps(incident)
        )
        reply = json.loads(resp.data.decode())

        self.assertTrue(reply)
        self.assertEqual(resp.status_code, 201)


    def test_create_red_flag_error(self):
        incident = dict(
        incidenceType = "Red flag",
        location = "752, 67056",
        comment = "corruption at icc",
        user_id = 1

        )
        resp = app.test_client(self).post(
            "api/v1/red-flags",
            content_type="application/json",
            data=json.dumps(incident)
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(reply["message"], "Incidence already captured!")
        self.assertEqual(resp.status_code, 400)
    
    def test_create_red_flag_with_blank_fieled(self):
        incident = dict(
        incidenceType = "",
        location = "752, 67056",
        comment = "",
        user_id = 1
        )
        resp = app.test_client(self).post(
            "api/v1/red-flags",
            content_type="application/json",
            data=json.dumps(incident)
        )
        reply = json.loads(resp.data.decode())
        self.assertIn(reply["message"], "All fields must be filled!")
        self.assertEqual(resp.status_code, 400)
    
    def test_get_all_red_flags(self):
        resp = app.test_client(self).get(
            "api/v1/red-flags"
        )
        reply = json.loads(resp.data.decode())
        self.assertTrue(reply)
        self.assertEqual(resp.status_code, 200)
        
    def test_get_specific_red_flag(self):
        resp = app.test_client(self).get(
            "api/v1/red-flags/1"
        )
        reply = json.loads(resp.data.decode())
        self.assertTrue(reply)
        self.assertEqual(resp.status_code, 400)

    def test_delete_specific_red_flag(self):
        resp = app.test_client(self).delete(
            "api/v1/red-flags/1"
        )
        reply = json.loads(resp.data.decode())
        self.assertTrue(reply)
        self.assertEqual(resp.status_code, 200)
