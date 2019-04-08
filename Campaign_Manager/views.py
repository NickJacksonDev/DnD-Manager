from django.shortcuts import render, redirect
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
from Users.models import *
from .urls import *

def home(request):
    form = CreateCampaignForm(request.POST or None)

    if form.is_valid():
        form.instance.creator = request.user
        form.save()
        return HttpResponseRedirect(reverse('campaign-list'))



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


def overview(request, pk=None ):

    #hazy on this. I want to set the campaign to the campaign ref'd by the pk
    campaign = Campaign.objects.get(pk=pk)
    party, created = Party.objects.get_or_create(campaign = campaign)
    members = party.members.all()
    friend, created = Friend.objects.get_or_create(current_user=request.user)
    friends = friend.users.all()
    friends |= User.objects.filter(pk = request.user.pk)

    friendCharacters = None
    for friend in friends:
        if friendCharacters == None:
            friendCharacters = Character.objects.filter(user = friend)
        else:
            friendCharacters |= Character.objects.filter(user = friend)
    posts = CampaignComment.objects.filter(campaign = campaign)
    dms = CampaignDM.objects.filter(campaign = campaign)
    userIsDM = False
    for dm in dms:
        if dm.user == request.user:
            userIsDM = True


    context ={

        'campaign' : campaign,
        #'users' : User.objects.exclude(id=request.user.id),
        'campaigns' : Campaign.objects.all(),
        'characters' : Character.objects.all(),
        'title' : 'Overview',
        'members' : members,
        'friends' : friends,
        'dms' : dms,
        'userIsDM' : userIsDM,
        'posts' : posts,
        'friendCharacters' : friendCharacters,

    }

    return render(request, 'Campaign_Manager/overview.html', context)

def update_party(request, operation, pk, id):
    new_member = Character.objects.get(pk=pk)
    campaign = Campaign.objects.get(pk=id)
    if operation == 'add':
        Party.add_member(campaign, new_member)
    elif operation == 'remove':
        Party.remove_member(campaign, new_member)
    return redirect('overview_with_pk', pk=campaign.pk)

def confirmDeletion(request, pk):
    campaign = Campaign.objects.get(pk=pk)

    context = {
        'campaign' : campaign,

    }

    return render(request, 'Campaign_Manager/campaign_confirm_deletion.html', context)


def deleteCampaign(request, pk):
    campaign = Campaign.objects.get(pk=pk)
    #Campaign.objects.delete(campaign)
    campaign.delete()
    return redirect('campaign-list')

class CampaignListView(ListView):
    model = Campaign
    context_object_name = 'campaigns'


class CampaignDetailView(DetailView):
    model = Campaign

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        campaign=self.get_object()
        context['posts'] = CampaignComment.objects.filter(campaign=campaign)
        dms = CampaignDM.objects.filter(campaign=campaign)
        context['userIsDM'] = False
        for dm in dms:
            if dm.user == self.request.user:
                context['userIsDM'] = True

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
        campaign=Campaign.objects.get(pk=self.kwargs.get('pk'))
        dms = CampaignDM.objects.filter(campaign=campaign)
        context['userIsDM'] = False
        for dm in dms:
            if dm.user == self.request.user:
                context['userIsDM'] = True

        return context

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.campaign = Campaign.objects.get(campaignID=self.kwargs['pk'])
        f.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('overview_with_pk', kwargs={'pk':self.kwargs['pk']})


class CampaignCommentDetailView(DetailView):
    model = CampaignComment

    def get_context_data(self, **kwargs):
        context=super(CampaignCommentDetailView, self).get_context_data(**kwargs)
        context['post'] = self.get_object()
        context['author'] = self.get_object().author
        return context

class CampaignCommentEditView(UpdateView):
    model = CampaignComment
    form_class = CreatePostForm

    def get_context_data(self, **kwargs):
        context = super(CampaignCommentEditView, self).get_context_data(**kwargs)
        campaign=Campaign.objects.get(pk=self.kwargs.get('fk'))
        context['dms']=CampaignDM.objects.filter(campaign=campaign)
        return context

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.campaign = Campaign.objects.get(campaignID=self.kwargs['fk'])
        f.save()
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('overview_with_pk', kwargs={'pk':self.kwargs['fk']})


class CampaignCommentDeleteView(DeleteView):
    model = CampaignComment

    def get_context_data(self, **kwargs):
        context=super(CampaignCommentDeleteView, self).get_context_data(**kwargs)
        context['post'] = self.get_object()
        context['author'] = self.get_object().author
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('overview_with_pk', kwargs={'pk':self.kwargs['fk']})
