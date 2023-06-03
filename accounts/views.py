from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from django.contrib import messages

# Create your views here.

# Register
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/login/")
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

# Login
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if not request.user.is_authenticated:
        if request.method == "POST":

            if form.is_valid():
                user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
                if user is not None:
                    login(request, user)
                    return redirect('scheduled_events')
                else:
                    messages.error(request, 'Invalid credentials.')
            else:
                messages.error(request, 'Error validating the form.')
        return render(request, "accounts/login.html", {"form": form, "msg": msg})
    return redirect("scheduled_events")

@login_required()
def logout_view(request):
    logout(request)
    return redirect('/login/')


