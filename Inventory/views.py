from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.http import HttpResponseRedirect
from .models import *
from .forms import CreateItemForm

# Home view
def home(request):
    form = CreateItemForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
            'title' : 'Inventory',
            'items' : Item.objects.all(),
            'form' : form
    }

    return render(request, 'Inventory/item-home.html', context)

# This is a class based view that uses django's built-in
# ListView view to display the inventorys
# It inherits from ListView
class ItemListView(ListView): 
    model = Item
    # template_name = 'InventoryBuilder/Inventory_builder-home.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    # context_object_name = 'inventorys'
    #context_object_name = 'items'


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['itemName']
    # exclude = []

    login_url = '/login/'

    # def __init__(self, *args, **kwargs):
    #   form.instance.user = self.request.user

    def form_valid(self, form):
        # Updates the author of the current form to be the current user
        form.instance.user = self.request.user 
        return super().form_valid(form)


class ItemEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ['itemName']
    # exclude = []

    login_url = '/login/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Tests to ensure the logged-in user is the owner of that inventory...
    def test_func(self):
        Item = self.get_object()
        if self.request.user == Item.user:
            return True
        return False


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = '/inventory/inventory'
    login_url = '/login/'
    fail_url = '/login/' #Works?

    def test_func(self):
        Item = self.get_object()
        if self.request.user == Item.user:
            return True
        return False
