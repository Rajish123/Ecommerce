from django import template

register = template.Library()

@register.filter(name = 'is_in_cart')
# cart is dictionary {'product_id':quantity}
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            # if product already added in cart
            return True
    return False

@register.filter(name = 'cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            # returns value i.e, quantity
            return cart.get(id)
    return 0;