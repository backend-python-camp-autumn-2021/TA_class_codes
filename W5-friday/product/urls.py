from django.urls import path

from .views import list_product

urlpatterns = [
    path('list/', list_product, name="list")
]
