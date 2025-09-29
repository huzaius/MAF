from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile

class UserAppTests(TestCase):

    def setUp(self):
        """Set up a test user and client for all tests."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword123')
        self.user_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpassword123',
        }

    def test_user_profile_created_on_user_creation(self):
        """Test that a UserProfile is created automatically when a User is created."""
        self.assertTrue(hasattr(self.user, 'userprofile'))
        self.assertIsInstance(self.user.userprofile, UserProfile)

    def test_register_view(self):
        """Test the user registration view."""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302) # Should redirect on success
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_account_view_authenticated(self):
        """Test that an authenticated user can access the account page."""
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/account.html')

    def test_account_view_unauthenticated(self):
        """Test that an unauthenticated user is redirected from the account page."""
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/users/account/')

    def test_delete_account_view_unauthenticated(self):
        """Test that an unauthenticated user is redirected from the delete account page."""
        response = self.client.get(reverse('delete_account'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/users/account/delete/')

    def test_delete_account_view_post_correct_password(self):
        """Test that a user can delete their account with the correct password."""
        self.client.login(username='testuser', password='testpassword123')
        user_count_before = User.objects.count()
        response = self.client.post(reverse('delete_account'), {'password': 'testpassword123'})
        
        self.assertEqual(User.objects.count(), user_count_before - 1)
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertRedirects(response, reverse('qnahub-home'))

    def test_delete_account_view_post_incorrect_password(self):
        """Test that an error is shown if the user provides an incorrect password."""
        self.client.login(username='testuser', password='testpassword123')
        user_count_before = User.objects.count()
        response = self.client.post(reverse('delete_account'), {'password': 'wrongpassword'})
        
        self.assertEqual(User.objects.count(), user_count_before) # User should not be deleted
        self.assertEqual(response.status_code, 200) # Should re-render the page with an error
        self.assertContains(response, 'Incorrect password. Please try again.')
