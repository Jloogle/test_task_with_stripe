from django.urls import include, path
from rest_framework import routers

from api.views import ItemViewSet, buy


router = routers.SimpleRouter()
router.register(r'item', ItemViewSet, basename='item')

app_name = 'api'

urlpatterns = [
    path('buy/<int:pk>/', buy, name='buy'),
    path('', include(router.urls)),
]
