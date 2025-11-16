from django.shortcuts import render

def personal(request):
    return render(request, "personalAccount/client_info.html")


# Create your views here.