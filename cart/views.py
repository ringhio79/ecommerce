from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product

# Create your views here.

def remove_item(request):
    id = request.POST['id']
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')
    

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items=[]
    grand_total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        grand_total += item_total
        cart_items.append({'product':product, 'quantity': quantity, 'item_total': item_total})
        
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'grand_total': grand_total})

def add_to_cart(request):
    product_id = request.POST['id']
    quantity = int(request.POST['quantity'])
    
    cart = request.session.get('cart', {})
# update the cart
    cart[product_id] = cart.get(product_id, 0) +quantity
# save the cart back into the session
    request.session['cart'] = cart
    
    return redirect('product_list')
    
