from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from Character_Builder.models import Character
from Campaign_Manager.models import Campaign
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CreateCampaignForm, CreatePostForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    form = CreateCampaignForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
            'title' : 'Campaigns',
            'campaigns' : Campaign.objects.all(),
            'characters' : Character.objects.all(),
            'partys' : Party.objects.all(),
            'partyCharacters' : PartyCharacter.objects.all(),
            'campaignDMs' : CampaignDM.objects.all(),
            'form' : form,
            'posts': CampaignComment.objects.all(),
    }

    return render(request, 'Campaign_Manager/campaign_builder.html', context)


class CampaignListView(ListView):
    model = Campaign
    context_object_name = 'campaigns'


class CampaignDetailView(DetailView):
    model = Campaign

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['posts'] = CampaignComment.objects.all()
        return context


class CampaignCreateView(CreateView):
    model = Campaign
    fields = ['campaignName']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class CampaignCommentCreateView(CreateView):
    model = CampaignComment
    form_class = CreatePostForm

    def get_context_data(self, **kwargs):
        context = super(CampaignCommentCreateView, self).get_context_data(**kwargs)
        context['campaignID']=Campaign.objects.filter(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.campaign = Campaign.objects.get(campaignID=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('campaign-detail', kwargs={'pk':self.kwargs['pk']})


class CampaignCommentDetailView(DetailView):
    model = CampaignComment

    def get_context_data(self, **kwargs):
        context=super(CampaignCommentDetailView, self).get_context_data(**kwargs)
        context['post'] = CampaignComment.objects.get(slug=self.kwargs['slug'])
        return context


class CampaignCommentEditView(UpdateView):
    model = CampaignComment
    form_class = CreatePostForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == Character.user:
            return True
        return False


class CampaignCommentDeleteView(DeleteView):
    model = CampaignComment

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('campaign-detail', kwargs={'pk':self.kwargs['pk']})