from django.urls import path
from .views import PasswordsChangeView, UserRegisterView, UserUpdateView, password_success, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='register'),
   path('update_profile/', UserUpdateView.as_view(), name='edit_user'),
   # path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change_password.html')),
   path('password/', PasswordsChangeView.as_view(template_name = 'registration/change_password.html')),
   path('password_success/',views.password_success, name='password_success'),
   path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
   path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='profile_page_edit'),
   path('create_profile_page/', CreateProfilePageView.as_view(), name='profile_page_create'),

]