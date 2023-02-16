from django.urls import path

from .views import ItemView, buy

app_name = 'payments'

urlpatterns = [
    path('buy/<int:pk>/', buy, name='buy'),
    path('item/<int:pk>/', ItemView.as_view(), name='item')
]
