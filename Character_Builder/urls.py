from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='character_builder-home'),
]