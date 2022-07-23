from django import template

register = template.Library()

# filter to show rupees in front of price,total
@register.filter(name = "currency")
def currency(number): 
    return "₹ " + str(number)

@register.filter(name = "multiply")
def multiply(price,quantity):
    return price * quantity

@register.filter(name = 'cart_count')
def cart_count(request):
    cart = request.session.get('cart').keys()
    return len(cart)   