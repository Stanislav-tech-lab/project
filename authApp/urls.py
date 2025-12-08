from django.urls import path
from .views import auth_page
from .views import logout_user

urlpatterns = [
    path('', auth_page, name='auth'),
    path("", logout_user, name="logout"),
]
