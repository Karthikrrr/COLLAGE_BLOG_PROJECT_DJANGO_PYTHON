from django.urls import path
from .views import UserRegisterView, UserUpdateProfile

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='register'),
   path('update-profile/', UserUpdateProfile.as_view(), name='edit_user'), 
]