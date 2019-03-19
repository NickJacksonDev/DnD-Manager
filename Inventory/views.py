from django.shortcuts import render
from .models import *
from Character_Builder.models import Character
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CreateItemForm
from django.views.generic import CreateView

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

    return render(request, 'Inventory/inventory-home.html', context)

# Creation form view
class ItemCreateView(CreateView):
    model = Item
    fields = ['itemName']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
