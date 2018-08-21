from django.shortcuts import render, redirect

# Create your views here.
def add_to_cart(request):
    product_id = request.POST['id']
    quantity = int(request.POST['quantity'])
    
    cart = request.session.get('cart', {})
# update the cart
    cart[product_id] = cart.get(product_id, 0) +quantity
# save the cart back into the session
    request.session['cart'] = cart
    
    print(cart)
    
    return redirect('product_list')
    
def view_cart(request):
    return render(request, 'cart/view_cart.html')