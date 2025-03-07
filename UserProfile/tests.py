from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileTests(TestCase):
    def setUp(self):
        """
        Set up initial test data for the tests.
        """
        # Create a test user for login tests
        self.test_user = User.objects.create_user(
            email_address='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def test_user_create(self):
        """
        Test that a new user can register successfully.
        """
        # Simulate a POST request to create a new user
        response = self.client.post(reverse('user_create'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'birthdate': '1990-01-01',
            'sex_at_birth': 'M',
            'email_address': 'johndoe@example.com',
            'password1': 'password123',
            'password2': 'password123',
            'expression_of_consent': True,
            'declaration_undertaking': True,
        })

        # Check if the user was successfully created
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertRedirects(response, reverse('user_login'))  # Check the redirect target
        self.assertTrue(User.objects.filter(email_address='johndoe@example.com').exists())  # User exists in the database

    def test_login_with_email(self):
        """
        Test that a user can log in using their email address and password.
        """
        # Simulate a POST request to log in with email address
        response = self.client.post(reverse('user_login'), {
            'username': 'testuser@example.com',  # Use email_address here
            'password': 'password123',
        })

        # Check if the login is successful and redirects to the dashboard
        self.assertEqual(response.status_code, 302)  # Should redirect to dashboard
        self.assertRedirects(response, reverse('dashboard'))  # Check the redirect target
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # User should be authenticated

    def test_invalid_login(self):
        """
        Test that invalid login credentials return an error.
        """
        # Attempt to log in with incorrect credentials
        response = self.client.post(reverse('user_login'), {
            'username': 'wrongemail@example.com',
            'password': 'wrongpassword',
        })

        # Check if the login page reloads with an error message
        self.assertEqual(response.status_code, 200)  # Page reloads on error
        self.assertContains(response, "Invalid email or password.")  # Check for error message
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # User should not be authenticated
