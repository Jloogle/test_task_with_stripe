from django.conf import settings
from django.views.generic import TemplateView

from api.views import ItemViewSet


class ItemView(TemplateView):
    template_name = 'buy_item.html'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        view = ItemViewSet.as_view({'get': 'retrieve'})
        response = view(request=self.request, pk=self.kwargs['pk'])
        item = response.data
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context
