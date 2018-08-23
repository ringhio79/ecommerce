from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import OrderLineItem
from products.models import Product


# Create your views here.
def view_checkout(request):
    if request.method == "POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            cart=request.session.get('cart', {})
            for product_id, quantity in cart.items():
                lineItem=OrderLineItem(order=order, quantity=quantity, product_id = product_id)
                lineItem.save()
                
            del request.session['cart']
        return redirect("home")
    else: 
        form=OrderForm()
    
    cart = request.session.get('cart', {})
    cart_items=[]
    grand_total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        grand_total += item_total
        cart_items.append({'product':product, 'quantity': quantity, 'item_total': item_total})
        
    return render(request, 'checkout/view_checkout.html', {'form': form, 'cart_items': cart_items, 'grand_total': grand_total})