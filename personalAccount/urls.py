from django.urls import path
from . import views

urlpatterns = [
    path("personalAccount/", views.personal_account, name="personal_account"),
    
]