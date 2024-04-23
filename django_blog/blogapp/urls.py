from django.urls import path
from . import views
from .views import CategoryView, HomeView , PostDetailView, AddBlogView, UpdateBlogView, DeleteBlogView, LikeView




urlpatterns = [
    path('' , HomeView.as_view(), name='home'),
    path('blog/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddBlogView.as_view(), name='add_post'),
    path('blog/update/<int:pk>', UpdateBlogView.as_view(), name='update_post' ),
    path('blog/<int:pk>/delete', DeleteBlogView.as_view(), name='delete_post' ),
    path('category/<str:cats>/' , CategoryView , name='category'),
    path('like/<int:pk>' , LikeView, name='like_post'),

]