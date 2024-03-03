from django.urls import path
from . import views
from .views import HomeView , PostDetailView, AddBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    path('' , HomeView.as_view(), name='home'),
    path('blog/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddBlogView.as_view(), name='add_post'),
    path('blog/update/<int:pk>', UpdateBlogView.as_view(), name='update_post' ),
    path('blog/<int:pk>/delete', DeleteBlogView.as_view(), name='delete_post' ),
#     path("register" , views.register , name="register"),
#     path("login" , views.user_login , name="login"),
#     path("signout" , views.signout, name="signout"),
]