import stripe
from django.contrib import messages



def charge_card(amount, stripe_token, request):
    total_in_cent = int(amount*100)
    try:
        charge=stripe.Charge.create(
            amount=total_in_cent,
            currency="EUR",
            description="Dummy Transaction",
            card=stripe_token,
            )
        return charge
     
    except:
        messages.error(request, "Error Charging Credit Card")
    
   