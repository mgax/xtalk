from django.conf import settings
from django.contrib.auth import login, logout
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render

from xtalk.login import tokens

from .forms import LoginForm


def login_form(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            tokens.send(request, email)
            return render(request, "login/email_sent.html", {"email": email})

    else:
        form = LoginForm()

    return render(request, "login/form.html", {"form": form})


def check_token(request, token):
    user = tokens.check(token)
    if user is None:
        return HttpResponseNotFound()

    login(request, user)
    return redirect(settings.LOGIN_REDIRECT_URL)


def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
