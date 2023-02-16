import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['GET'])
def buy(request, pk):
    item = get_object_or_404(Item, pk=pk)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:4242/success',
        cancel_url='http://localhost:4242/cancel',
    )
    return Response({'id': session.id})


class ItemView(TemplateView):
    template_name = 'buy_item.html'

    def get_context_data(self, **kwargs):
        item_pk = self.kwargs['pk']
        item = get_object_or_404(Item, pk=item_pk)
        context = super(ItemView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context
