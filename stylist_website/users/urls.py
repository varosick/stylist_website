from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import (EmailVerificationView, UserForgotPasswordView,
                         UserGuideDetailView, UserGuidesView, UserLoginView,
                         UserPasswordResetConfirmView, UserProfileView,
                         UserRegistrationView, UserServiceDetailView,
                         UserServicesView, UsersReviewsView, user_logout)

app_name = 'users'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reviews/', UsersReviewsView.as_view(), name='reviews'),
    path('profile/my_services/', UserServicesView.as_view(), name='user_services'),
    path('profile/my_services/<int:pk>', UserServiceDetailView.as_view(), name='user_services_detail'),
    path('profile/my_guides/', UserGuidesView.as_view(), name='user_guides'),
    path('profile/my_guides/<slug:guide_slug>', UserGuideDetailView.as_view(), name='user_guide_detail'),
    path('profile/email_verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verify'),

    ]
