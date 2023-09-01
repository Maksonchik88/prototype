from django.shortcuts import render


def catalog(request):
    template = "catalog.html"
    return render(request, template)
