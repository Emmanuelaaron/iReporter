import unittest
from api import*
from api.views import app
from flask import json
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

        self.assertIn("You've, signed up sucessfully", reply)
        self.assertEqual(resp.status_code, 201)

    def test_signupuser_without_firstname(self):
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

        self.assertEqual(reply["message"], "firstname is required!")
        self.assertEqual(resp.status_code, 400)
    
    def test_signupuser_without_lastname(self):
        user = dict(
            firstname="Donald",
            lastname=" ",
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

        self.assertEqual(reply["message"], "lastname is required!")
        self.assertEqual(resp.status_code, 400)

    def test_signupuser_without_email(self):
        user = dict(
            firstname="Donald",
            lastname="Ngiya",
            othernames="Danny",
            email="",
            password="ghgdhgd",
            username="dojo"
        )

        resp = app.test_client(self).post(
            "api/v1/signup",
            content_type="application/json",
            data=json.dumps(user)
        )

        reply = json.loads(resp.data.decode())

        self.assertEqual(reply["message"], "email is required!")
        self.assertEqual(resp.status_code, 400)

    def test_signupuser_without_password(self):
        user = dict(
            firstname="donald",
            lastname="ngiya",
            othernames="Danny",
            email="ngisd@gmail.com",
            password="",
            username="dojo"
        )

        resp = app.test_client(self).post(
            "api/v1/signup",
            content_type="application/json",
            data = json.dumps(user)
        )
        reply = json.loads(resp.data.decode())

        self.assertEqual(reply["message"], "password is required!")
        self.assertEqual(resp.status_code, 400)

