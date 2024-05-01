from django.urls import path
from . import views

app_name = "Comunidad"

urlpatterns = [
    path('', views.home, name="home"),
]