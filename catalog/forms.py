from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu nombre'
        })
    )
    correo = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu correo'
        })
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu mensaje',
            'rows': 5
        })
    )
