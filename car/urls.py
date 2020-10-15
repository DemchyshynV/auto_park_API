from django.urls import path
from .views import CarCreateView

urlpatterns = [
    path('', CarCreateView.as_view())
]
