from django.shortcuts import render

def index(request):
    return render(request, "indexApp/indexApp.html")


# Create your views here.
