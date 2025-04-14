from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignupForm


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log the user in
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})
