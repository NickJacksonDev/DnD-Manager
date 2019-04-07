from django.urls import path
from .views import (
    CharacterListView,
    CharacterDetailView,
    CharacterCreateView,
    CharacterEditView,
    CharacterDeleteView,

    CharacterRaceListView,
)
from . import views

urlpatterns = [
    path('', views.home, name='character_builder-home'),
    # path('', PostListView.as_view(), name='character_builder-home'),
    path('characters/', CharacterListView.as_view(), name='character-list'),
    path('characters/create/', CharacterCreateView.as_view(), name='character-create'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('characters/<int:pk>/edit', CharacterEditView.as_view(), name='character-edit'),
    path('characters/<int:pk>/delete', CharacterDeleteView.as_view(), name='character-delete'),
    path('races/', CharacterRaceListView.as_view(), name='characterRace-list'),
]

