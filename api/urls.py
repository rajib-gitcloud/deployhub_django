from django.urls import path
from .views import HealthCheckView, InfoView, ItemListView

urlpatterns = [
    path('', HealthCheckView.as_view(), name='root-health'),
    path('api/health/', HealthCheckView.as_view(), name='health-check'),
    path('api/info/', InfoView.as_view(), name='app-info'),
    path('api/items/', ItemListView.as_view(), name='item-list'),
]
