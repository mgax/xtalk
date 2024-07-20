from django.shortcuts import render


def room(request, room):
    return render(request, "room.html", {"room": room})
