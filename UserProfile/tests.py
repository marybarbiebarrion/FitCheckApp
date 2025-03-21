from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from parameterized import parameterized

User = get_user_model()

class UserProfileTests(TestCase):
    def setUp(self):
        """
        Set up reusable test data for all tests.
        """
        # Create a reusable test user for login/logout tests
        self.test_user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123',
            first_name='Test',
            last_name='User'
        )

    def create_user_data(self, username=None, email=None):
        """
        Helper method to generate dynamic user data for tests.
        """
        return {
            'username': username or 'johndoe',
            'first_name': 'John',
            'last_name': 'Doe',
            'birthdate_month': '1',  # January
            'birthdate_day': '1',   # 1st
            'birthdate_year': '1990',  # 1990
            'sex_at_birth': 'M',
            'email': email or 'johndoe@example.com',
            'password1': 'Str0ngP@ssw0rd!',
            'password2': 'Str0ngP@ssw0rd!',
            'expression_of_consent': True,
            'declaration_undertaking': True,
        }

    def test_user_create(self):
        """
        Test that a new user can register successfully.
        """
        user_data = self.create_user_data()
        response = self.client.post(reverse('user_create'), user_data)

        # Debugging: Print the response content
        print(response.content.decode())  # Decode the response content to make it readable

        # Assertions
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertTrue(User.objects.filter(username='johndoe').exists())  # User exists in the database

    def test_login_with_username(self):
        """
        Test that a user can log in using their username and password.
        """
        response = self.client.post(reverse('user_login'), {
            'username': self.test_user.username,
            'password': 'password123',
        })

        # Assertions
        self.assertEqual(response.status_code, 302)  # Should redirect to dashboard
        self.assertRedirects(response, reverse('dashboard'))  # Check the redirect target
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # User should be authenticated

    def test_invalid_login(self):
        """
        Test that invalid login credentials return an error.
        """
        response = self.client.post(reverse('user_login'), {
            'username': 'wrongusername',
            'password': 'wrongpassword',
        })

        # Assertions
        self.assertEqual(response.status_code, 200)  # Page reloads on error
        self.assertContains(response, "Invalid username or password.")  # Check for error message
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # User should not be authenticated

    def test_user_logout(self):
        """
        Test that a logged-in user can log out successfully.
        """
        self.client.login(username=self.test_user.username, password='password123')
        response = self.client.get(reverse('user_logout'))

        # Assertions
        self.assertEqual(response.status_code, 302)  # Should redirect to home page
        self.assertRedirects(response, reverse('home'))  # Check the redirect target
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # User should be logged out

    @parameterized.expand([
        ("missing_username", {'username': '', 'email': 'test@example.com'}, "Please enter a username."),
        ("missing_email", {'username': 'testuser', 'email': ''}, "Please enter an email address."),
        ("password_mismatch", {'password1': 'password123', 'password2': 'password456'}, "The two password fields didn’t match."),
        ("invalid_email", {'email': 'invalid-email'}, "Enter a valid email address."),
        ("missing_consent", {'expression_of_consent': False}, "You must agree to share your health data."),
    ])
    def test_user_create_validation_errors(self, name, invalid_data, expected_error):
        """
        Test user creation with invalid data to ensure proper validation errors.
        """
        user_data = self.create_user_data()
        user_data.update(invalid_data)  # Inject invalid data
        response = self.client.post(reverse('user_create'), user_data)
    
        # Assertions
        self.assertEqual(response.status_code, 200)  # Form should reload with errors
        self.assertContains(response, expected_error)  # Check for specific validation error

    def test_duplicate_username(self):
        """
        Test that creating a user with a duplicate username fails.
        """
        User.objects.create_user(username='johndoe', email='johndoe@example.com', password='password123')
        user_data = self.create_user_data(username='johndoe')
        response = self.client.post(reverse('user_create'), user_data)

        # Debugging: Print the response content
        print(response.content.decode())  # Decode the response content to make it readable

        # Assertions
        self.assertEqual(response.status_code, 200)  # Form should reload with errors
        self.assertContains(response, "The username you entered is already taken.")

    def test_duplicate_email(self):
        """
        Test that creating a user with a duplicate email fails.
        """
        user_data = self.create_user_data(username='newuser', email='testuser@example.com')
        response = self.client.post(reverse('user_create'), user_data)

        # Assertions
        self.assertEqual(response.status_code, 200)  # Form should reload with errors
        self.assertContains(response, "A user with this Email Address already exists.")  # Check for duplicate email error
