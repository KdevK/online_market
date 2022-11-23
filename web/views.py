from django.http import HttpResponse
from django.shortcuts import render, redirect
import stripe

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from online_market.settings import HOST
from web.models import Item


def main_view(request):
    context = {"items": Item.objects.all()}
    return render(request, "main.html", context=context)


class ItemDetailView(DetailView):
    model = Item
    template_name = "item.html"


def pay_view(request, pk):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': Item.objects.filter(id=pk).first().name,
                    'description': Item.objects.filter(id=pk).first().description,
                },
                'unit_amount': int(Item.objects.filter(id=pk).first().price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=HOST+'/success',
        cancel_url=HOST+'/cancel',
    )

    return HttpResponse(session['id'])


def success_view(request):
    return render(request, "success.html")


def cancel_view(request):
    return render(request, "cancel.html")
