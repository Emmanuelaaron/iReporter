import unittest
from api import*
from .views import app
from flask import json
# from api.models import Users

class TestAllRoutes(unittest.TestCase):
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
