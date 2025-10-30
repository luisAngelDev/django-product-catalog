from django.shortcuts import render,redirect
from .models import Product
from .forms import ContactForm

def product_list(request):
    products = Product.objects.all()
    mensaje_exito = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            mensaje_exito = "Mensaje enviado correctamente"
            form = ContactForm()  # limpia formulario
    else:
        form = ContactForm()

    return render(request, 'catalog/product_list.html', {
        'products': products,
        'form': form,
        'mensaje_exito': mensaje_exito,
    })
