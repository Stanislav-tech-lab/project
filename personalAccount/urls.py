from django.urls import path
from . import views

urlpatterns = [
    path("personalAccount/", views.personal, name="personal_account"),
    
]