from django.shortcuts import render


def index(request):
    template = "homepage.html"
    return render(request, template)
