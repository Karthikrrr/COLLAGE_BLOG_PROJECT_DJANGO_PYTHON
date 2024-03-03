from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_detailed_view.html'

class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blog.html'
    # fields = ('title' , 'author' , 'body')

class UpdateBlogView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_blog.html'

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'  
    success_url = reverse_lazy('home')

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