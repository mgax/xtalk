from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


@login_required
def room(request, room):
    return render(request, "room.html", {"room": room})
