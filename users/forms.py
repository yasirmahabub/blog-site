from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given username,
    email and password.
    """

    class Meta:
        model = User
        fields = ("username", "email")
