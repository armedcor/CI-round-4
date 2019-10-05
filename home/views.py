from django.shortcuts import render

def index(request):
    """A view that will display the landing page"""
    return render(request, "index.html")
