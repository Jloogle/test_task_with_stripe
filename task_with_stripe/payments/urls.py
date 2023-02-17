from django.urls import path

from .views import ItemView

app_name = 'payments'

urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view(), name='item')
]
