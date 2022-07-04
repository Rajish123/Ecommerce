from django import template

register = template.Library()

# filter to show rupees in front of price,total
@register.filter(name = "currency")
def currency(number): 
    return "₹ " + str(number)