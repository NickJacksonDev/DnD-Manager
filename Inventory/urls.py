from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemEditView,
    ItemDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='inventory-home'),
    path('inventory/', ItemListView.as_view(), name='item-list'),
    path('inventory/create/', ItemCreateView.as_view(), name='item-create'),
    path('inventory/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('inventory/<int:pk>/edit', ItemEditView.as_view(), name='item-edit'),
    path('inventory/<int:pk>/delete', ItemDeleteView.as_view(), name='item-delete'),
]