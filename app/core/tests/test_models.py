"""
test for model
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """
    test models
    """

    def test_create_user_with_email_successful(self):
        """test creating new user with email successfully ."""

        email = 'test@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """test email is normalized for new user ."""
        sample_email = [
            ['test1@Example.com', 'test1@example.com'],
            ['test2@exAMple.com', 'test2@example.com'],
            ['test3@example.com', 'test3@example.com'],
            ['test4@EXAMPLE.com', 'test4@example.com'],
        ]

        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email=email, password='sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_whitout_email_raise_error(self):
        """test that creating user without an email raise value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """test creating superuser. """
        user = get_user_model().objects.create_superuser(
            email='test@example.com',
            password='test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
