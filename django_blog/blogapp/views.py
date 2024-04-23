from django.contrib import messages
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdateForm
from django.http import HttpResponseRedirect


def LikeView(request , pk):
    post = get_object_or_404(Post , id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


def CategoryView(request , cats):
    category_post = Post.objects.filter(category=cats.replace('-' , ' '))
    return render(request, 'categories.html' , {'cats':cats.title().replace('-' , ' '), 'category_post':category_post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detailed_view.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu

        get_value = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = get_value.total_likes()
        context["total_likes"] = total_likes

        liked = False
        if get_value.likes.filter(id=self.request.user.id).exists():
            liked = True  
        context["liked"] = liked
        return context

class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blog.html'

class UpdateBlogView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_blog.html'

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'  
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(DeleteBlogView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context