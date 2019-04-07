from django.urls import path
from .views import (
    CampaignListView,
    CampaignDetailView,
)
from . import views

urlpatterns = [
    path('', views.home, name='campaign_builder-home'),
    path('campaigns/', CampaignListView.as_view(), name='campaign-list'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
]
