from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import signup_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
