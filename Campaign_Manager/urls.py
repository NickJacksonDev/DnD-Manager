from django.urls import path, reverse
from django.utils.text import slugify
from .views import (
    CampaignListView,
    CampaignDetailView,
    CampaignCommentCreateView,
    CampaignCommentDetailView,
    CampaignCommentEditView,
    CampaignCommentDeleteView,
)
from django.urls import path
from . import views

urlpatterns = [
    path('',
    	views.home, name='campaign_builder-home'),

    path('campaigns/',
    	CampaignListView.as_view(), name='campaign-list'),

    path('campaigns/<int:pk>/',
    	CampaignDetailView.as_view(), name='campaign-detail'),

    path('campaigns/<int:pk>/AddComment/', 
    	CampaignCommentCreateView.as_view(), name='campaign-comment'),

    path('campaigns/<int:fk>/<slug:slug>/',
    	CampaignCommentDetailView.as_view(), name='campaigncomment-detail'),

    path('campaigns/<int:fk>/<slug:slug>/edit',
    	CampaignCommentEditView.as_view(), name='campaigncomment-edit'),

    path('campaigns/<int:fk>/<slug:slug>/delete',
    	CampaignCommentDeleteView.as_view(), name='campaigncomment-delete'),
]
