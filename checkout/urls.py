from django.urls import path
from .views import view_checkout, confirm_checkout

urlpatterns = [
    path('checkout', view_checkout, name="view_checkout"),
    path('confirm', confirm_checkout, name="confirm_checkout"),
    
]