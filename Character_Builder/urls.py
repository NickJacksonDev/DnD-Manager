from django.urls import path
from .views import CharacterListView
from . import views

urlpatterns = [
    path('', views.home, name='character_builder-home'),
    # path('', PostListView.as_view(), name='character_builder-home'),
]