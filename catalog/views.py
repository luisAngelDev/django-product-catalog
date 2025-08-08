from django.shortcuts import render,redirect
from .models import Product
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    mensaje_exito = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            mensaje_exito = "Mensaje enviado correctamente"
            form = ContactForm()  # limpiar formulario
    else:
        form = ContactForm()

    return render(request, 'catalog/product_list.html', {
        'productos': products,
        'form': form,
        'mensaje_exito': mensaje_exito,
    })
