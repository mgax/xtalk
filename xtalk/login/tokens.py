import time

from django.conf import settings
from django.core.mail import send_mail
from django.core.signing import BadSignature, Signer
from django.http import HttpRequest
from django.urls import reverse

from .models import User

signer = Signer()


def send(request: HttpRequest, email):
    token = signer.sign_object({"login_with_email": email, "timestamp": time.time()})
    url = request.build_absolute_uri(reverse("login:check", kwargs={"token": token}))
    text = f"Please click this link to log in:\n\n{url}\n"
    send_mail(
        from_email=None,
        subject="Login token",
        message=text,
        recipient_list=[email],
    )


def check(token):
    try:
        payload = signer.unsign_object(token)

    except BadSignature:
        return None

    timestamp = payload["timestamp"]
    if time.time() - timestamp > settings.LOGIN_TOKEN_MAX_AGE:
        return None

    email = payload["login_with_email"]
    user = User.objects.filter(email=email).first()

    if user is None:
        return User.objects.create_user(email=email)

    if user.last_login and timestamp < user.last_login.timestamp():
        # Token is out of date, possible reuse attempt
        return None

    return user
