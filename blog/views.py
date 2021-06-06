from django.shortcuts import render
from django.http import HttpResponse

posts = [
     {
        "author": "Gusion",
        "title": "Gusion Quotes",
        "content": "The perfect combination of might and magic.",
        "date_posted": "June 06, 2021",
     },
     {
        "author": "Zilong",
        "title": "Zilong Quotes",
        "content": "Your whole body is a weak spot.",
        "date_posted": "June 06, 2021",
     },
 ]


def home(request):
    return render(request, "blog/home.html", {"posts": posts})

def about(request):
    return render(request, "blog/about.html")
