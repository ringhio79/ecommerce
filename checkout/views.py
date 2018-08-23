from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import OrderForm, PaymentForm
from .models import OrderLineItem
from products.models import Product
from cart.utils import get_cart_items_and_total
from django.conf import settings
import stripe 
from django.contrib import messages
from .utils import charge_card


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def view_checkout(request):
    order_form = OrderForm()
    payment_form = PaymentForm()
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    context.update({'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY})
    return render(request, 'checkout/view_checkout.html', context)
        
def confirm_checkout(request):
    order_form=OrderForm(request.POST)
    payment_form = PaymentForm(request.POST)
    
    if order_form.is_valid() and payment_form.is_valid():
        order = order_form.save()
        
        cart=request.session.get('cart', {})
        
        
        for product_id, quantity in cart.items():
            lineItem=OrderLineItem(order=order, quantity=quantity, product_id = product_id)
            lineItem.save()
        
        
        items_and_total = get_cart_items_and_total(cart)
        total = items_and_total['grand_total']
        stripe_token=payment_form.cleaned_data['stripe_id']
        
        
        
        charge = charge_card(total, stripe_token, request)
        
        if charge == None:
            return HttpResponse("Error creating charge")
            
        if charge.paid:
            messages.error(request, "You have successfully paid")
            del request.session['cart']
            return redirect("home")
        else:
            return HttpResponse("Charge Not Paid")
    
    else:
        cart=request.session.get('cart', {})
        context=get_cart_items_and_total(cart)
        context.update({'order_form': order_form})
        
        return render(request, 'checkout/view_checkout.html', context)