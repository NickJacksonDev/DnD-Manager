from django.urls import path, reverse, re_path
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
from django.conf.urls import url


urlpatterns = [
    path('',
    	views.home, name='campaign_builder-home'),

    path('campaigns/',
    	CampaignListView.as_view(), name='campaign-list'),

    #path('campaigns/<int:pk>/',
    	#CampaignDetailView.as_view(), name='campaign-detail'),
    path('campaigns/<int:pk>/',
        views.overview, name = 'overview_with_pk'),

    path('campaigns/<int:pk>/AddComment/',
    	CampaignCommentCreateView.as_view(), name='campaign-comment'),

    path('campaigns/<int:fk>/<slug:slug>/',
    	CampaignCommentDetailView.as_view(), name='campaigncomment-detail'),

    path('campaigns/<int:fk>/<slug:slug>/edit',
    	CampaignCommentEditView.as_view(), name='campaigncomment-edit'),

    path('campaigns/<int:fk>/<slug:slug>/delete',
    	CampaignCommentDeleteView.as_view(), name='campaigncomment-delete'),

    #re_path('campaigns/(?P<pk>\d+)/', views.overview, name='overview_with_pk'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/(?P<id>\d+)/$', views.update_party, name='update_party'),

    path('campaigns/<int:pk>/delete',
        views.confirmDeletion, name = 'confirm-delete'),

    path('campaigns/<int:pk>/delete/confirmed',
        views.deleteCampaign, name = 'campaign-delete'),
]
