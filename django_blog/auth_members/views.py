from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from auth_members.forms import PasswordChangingForm, SignUpForm, UpdateProfileForm

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('home')

def password_success(request):
    return render(request, 'registration/password_success.html')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserUpdateView(generic.UpdateView):
    form_class = UpdateProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user