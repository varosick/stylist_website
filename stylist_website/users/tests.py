from django.test import TestCase
from users.forms import (
    UserLoginForm, UserRegistrationForm, UserProfileForm,
    ServicePurchaseForm, ReviewAddForm, CustomPasswordChangeForm,
    UserForgotPasswordForm, UserSetNewPasswordForm
)
from users.models import User, ScheduleDate
from django.urls import reverse

class UserLoginFormTest(TestCase):
    def test_invalid_login(self):
        form_data = {'username': '', 'password': ''}
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())


class UserRegistrationFormTest(TestCase):
    def test_valid_registration(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'date_of_birth': '1990-01-01',
            'password1': 'password123',
            'password2': 'password123',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'date_of_birth': '1990-01-01',
            'password1': 'password123',
            'password2': 'password321',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


class UserProfileFormTest(TestCase):
    def test_valid_profile_update(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'email': 'johndoe@example.com',
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'email': 'invalid-email',
        }
        form = UserProfileForm(data=form_data)
        self.assertFalse(form.is_valid())


class ServicePurchaseFormTest(TestCase):
    def test_valid_service_purchase(self):
        ScheduleDate.objects.create(date="2023-10-01", is_booked=False)
        form_data = {'datetime_of_service': '2023-10-01 12:00'}
        form = ServicePurchaseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_service_purchase(self):
        form_data = {'datetime_of_service': '2023-99-99 99:99'}
        form = ServicePurchaseForm(data=form_data)
        self.assertFalse(form.is_valid())


class ReviewAddFormTest(TestCase):
    def test_valid_review(self):
        form_data = {'review': 'This is a great service!'}
        form = ReviewAddForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_review(self):
        form_data = {'review': ''}
        form = ReviewAddForm(data=form_data)
        self.assertFalse(form.is_valid())


class CustomPasswordChangeFormTest(TestCase):
    def test_valid_password_change(self):
        form_data = {
            'old_password': 'oldpassword',
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123'
        }
        form = CustomPasswordChangeForm(user=User(), data=form_data)
        self.assertTrue(form.is_valid())

    def test_mismatch_password(self):
        form_data = {
            'old_password': 'oldpassword',
            'new_password1': 'newpassword123',
            'new_password2': 'differentpassword'
        }
        form = CustomPasswordChangeForm(user=User(), data=form_data)
        self.assertFalse(form.is_valid())


class UserForgotPasswordFormTest(TestCase):
    def test_valid_forgot_password(self):
        form_data = {'email': 'test@example.com'}
        form = UserForgotPasswordForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form_data = {'email': 'invalid-email'}
        form = UserForgotPasswordForm(data=form_data)
        self.assertFalse(form.is_valid())


class UserSetNewPasswordFormTest(TestCase):
    def test_valid_password_reset(self):
        form_data = {
            'new_password1': 'newpassword123',
            'new_password2': 'newpassword123',
        }
        form = UserSetNewPasswordForm(user=User(), data=form_data)
        self.assertTrue(form.is_valid())

    def test_mismatch_password(self):
        form_data = {
            'new_password1': 'newpassword123',
            'new_password2': 'differentpassword',
        }
        form = UserSetNewPasswordForm(user=User(), data=form_data)
        self.assertFalse(form.is_valid())




class UserLoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login_success(self):
        response = self.client.post(reverse('users:login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:profile'))

    def test_login_failure(self):
        response = self.client.post(reverse('users:login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Имя пользователя или пароль введены неверно")


class UserRegistrationViewTest(TestCase):
    def test_registration_success(self):
        response = self.client.post(reverse('users:registration'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))

    def test_registration_failure(self):
        response = self.client.post(reverse('users:registration'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'password123',
            'password2': 'password321'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Пароли не совпадают")


class UserProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_profile_update(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('users:profile'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:profile'))


class UserReviewsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_review_submission(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('users:reviews'), {'review': 'Great service!'})
        self.assertEqual(response.status_code, 302)


class UserServicesViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_view_user_services(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('users:user_services'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мои услуги')
