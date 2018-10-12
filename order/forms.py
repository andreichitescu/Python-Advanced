from django import forms
from cart.cart import Cart

class CartAddProductForm(forms.Form):
    quantity = ''
    product = ''
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=255)
    #sa contina un Form cu produsul respectiv, cantitatea si alte campuri pentru ca userul sa completeze\
    #  First name, Last name, adresa de livrare