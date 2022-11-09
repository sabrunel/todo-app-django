# Utilities
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView


# Create your views here.
class Login(LoginView):
    """A view that displays a login form."""
    template_name = 'accounts/login.html' # overrides the default value (registration/login.html)
    next_page = reverse_lazy('tasks')
    redirect_authenticated_user = True

class Logout(LogoutView):
    """ A view that handles user logout and redirects them to the login page."""
    next_page = reverse_lazy('login')


class Signup(FormView):
    """A view that displays a signup form and logs in users when successfully signed up."""
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form): 
        """ Overrides the method to login successfully registered users. """
        user = form.save()

        if user is not None:
            login(self.request, user)
        
        return super(Signup, self).form_valid(form)

    def get(self, *args, **kwargs):
        """ Overrides the method to mimick LoginView's redirect_authenticated_user = True."""
        if self.request.user.is_authenticated:
            return redirect('tasks')

        return super(Signup, self).get(*args, **kwargs)
        
