from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

# Create your views here.

def view_cart(request):
    
    cart = request.session.get('cart', {})
    
    cart_items=[]
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        cart_items.append({'product':product, 'quantity': quantity})
        
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

def add_to_cart(request):
    product_id = request.POST['id']
    quantity = int(request.POST['quantity'])
    
    cart = request.session.get('cart', {})
# update the cart
    cart[product_id] = cart.get(product_id, 0) +quantity
# save the cart back into the session
    request.session['cart'] = cart
    
    return redirect('product_list')
    
