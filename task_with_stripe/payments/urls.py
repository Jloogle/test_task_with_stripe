from django.urls import path

from .views import ItemBuyView, buy

app_name = 'payments'

urlpatterns = [
    path('buy/<int:pk>/', buy, name='buy'),
    path('item/<int:pk>/', ItemBuyView.as_view(), name='item')
]
