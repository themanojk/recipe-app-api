from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successfull"""
        email = 'manoj@gmail.com'
        password = 'Manoj@12343'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email of new user is normalized"""
        email = "manoj@GMAIL.com"

        user = get_user_model().objects.create_user(email=email)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email throws error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_super_user(
            email='super@admin.com',
            password='Admin@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
