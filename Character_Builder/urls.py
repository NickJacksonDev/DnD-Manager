from django.urls import path
from .views import CharacterListView, CharacterDetailView
from . import views

urlpatterns = [
    path('', views.home, name='character_builder-home'),
    # path('', PostListView.as_view(), name='character_builder-home'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
]