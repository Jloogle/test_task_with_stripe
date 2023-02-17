from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', include('payments.urls', namespace='payments')),
    path('api/', include('api.urls', namespace='api')),
]
