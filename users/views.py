from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    
    # If register button was clicked that triggers POST.
    # Let's save their input so if there is an invalid
    # field, we display it again.
    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")

            messages.success(request, "Account created for {}".format(username))
            return redirect("blog-home")

    # Else, the user simply routes to this page.    
    # We display an empty form.
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})
