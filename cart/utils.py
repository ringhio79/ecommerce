from products.models import Product
from django.shortcuts import get_object_or_404

def get_cart_items_and_total(cart):
    cart_items=[]
    grand_total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        item_total = product.price * quantity
        grand_total += item_total
        cart_items.append({'product':product, 'quantity': quantity, 'item_total': item_total})
    
    return {'cart_items': cart_items, 'grand_total': grand_total}