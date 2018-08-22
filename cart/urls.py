from django.urls import path
from .views import add_to_cart, view_cart, remove_item

urlpatterns = [
    path('add', add_to_cart, name="add_to_cart"),
    path('view', view_cart, name="view_cart"),
    path('remove', remove_item, name="remove_item"),
]