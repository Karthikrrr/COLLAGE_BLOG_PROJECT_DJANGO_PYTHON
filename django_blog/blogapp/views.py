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

# def register(request):
     
#      if request.method == "POST":
#          username = request.POST['username']
#          email = request.POST['email']
#          password = request.POST['password']
#          confirm_password = request.POST['confirmpassword']

#          if User.objects.filter(username=username):
#             messages.error(request, "Username already exist! Please try some other username.")
#             return redirect('/register')

#          if User.objects.filter(email=email).exists():
#             messages.error(request, "Email Already Registered!!")
#             return redirect('/register')
         
#          if len(username)>20:
#             messages.error(request, "Username must be under 20 charcters!!")
#             return redirect('/register')
         
#          if password != confirm_password:
#              messages.error(request, "Passwords didn't matched!!")
#              return redirect('/register')
         
#          if not username.isalnum():
#             messages.error(request, "Username must be Alpha-Numeric!!")
#             return redirect('/register')
         
#          myuser = User.objects.create_user(username=username, email=email, password=password)
#          myuser.save()
#          messages.success(request, "Your Account has been created succesfully!!")
#          return redirect('/login')
#      return render(request , "register.html")

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         true_user = authenticate(username=username, password=password)
        
#         if true_user is not None:
#             login(request , true_user)
#             get_username = true_user.username
#             messages.success(request, "Logged In Sucessfully!!")
#             return render(request, "home.html",{"first_name":get_username})
#         else:
#             messages.error(request, "Invalid Credentials!!")
#             return redirect('/login')
    
#     return render(request, "login.html")

# def signout(request):
#     logout(request)
#     messages.success(request, "Logged Out Successfully!!")
#     return redirect('home')def register(request):
     
#      if request.method == "POST":
#          username = request.POST['username']
#          email = request.POST['email']
#          password = request.POST['password']
#          confirm_password = request.POST['confirmpassword']

#          if User.objects.filter(username=username):
#             messages.error(request, "Username already exist! Please try some other username.")
#             return redirect('/register')

#          if User.objects.filter(email=email).exists():
#             messages.error(request, "Email Already Registered!!")
#             return redirect('/register')
         
#          if len(username)>20:
#             messages.error(request, "Username must be under 20 charcters!!")
#             return redirect('/register')
         
#          if password != confirm_password:
#              messages.error(request, "Passwords didn't matched!!")
#              return redirect('/register')
         
#          if not username.isalnum():
#             messages.error(request, "Username must be Alpha-Numeric!!")
#             return redirect('/register')
         
#          myuser = User.objects.create_user(username=username, email=email, password=password)
#          myuser.save()
#          messages.success(request, "Your Account has been created succesfully!!")
#          return redirect('/login')
#      return render(request , "register.html")

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         true_user = authenticate(username=username, password=password)
        
#         if true_user is not None:
#             login(request , true_user)
#             get_username = true_user.username
#             messages.success(request, "Logged In Sucessfully!!")
#             return render(request, "home.html",{"first_name":get_username})
#         else:
#             messages.error(request, "Invalid Credentials!!")
#             return redirect('/login')
    
#     return render(request, "login.html")

# def signout(request):
#     logout(request)
#     messages.success(request, "Logged Out Successfully!!")
#     return redirect('home')