from django.urls import path, re_path
from .views import (
    CampaignListView,
    CampaignDetailView,
)
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.home, name='campaign_builder-home'),
    path('campaigns/', CampaignListView.as_view(), name='campaign-list'),
    path('campaigns/<int:pk>/', CampaignDetailView.as_view(), name='campaign-detail'),
    re_path('campaigns/(?P<pk>\d+)/', views.overview, name='overview_with_pk'),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/(?P<id>\d+)/$', views.update_party, name='update_party')
]
