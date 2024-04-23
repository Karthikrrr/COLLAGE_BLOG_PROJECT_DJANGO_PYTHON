from django.urls import path
from .views import PasswordsChangeView, UserRegisterView, UserUpdateView, password_success
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='register'),
   path('update_profile/', UserUpdateView.as_view(), name='edit_user'),
   # path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html')),
   path('password/', PasswordsChangeView.as_view(template_name = 'registration/change_password.html')),
   path('password_success/',views.password_success, name='password_success'),
]