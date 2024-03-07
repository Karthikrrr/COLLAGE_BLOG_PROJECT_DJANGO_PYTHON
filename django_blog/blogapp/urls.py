from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("" , views.home, name="home"),
    path("register" , views.register , name="register"),
    path("login" , views.user_login , name="login"),
    path("signout" , views.signout, name="signout"),
] 