from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


User= get_user_model()

class UserTestCase(TestCase):

	def setUp(self):

		user_a= User(username="test", email="test.test.com")
		user_a.set_password("somepassword")
		user_a.save()