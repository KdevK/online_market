from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from web.models import Item


def main_view(request):
    context = {"items": Item.objects.all()}
    return render(request, "main.html", context=context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "item.html"
