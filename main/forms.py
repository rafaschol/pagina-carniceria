from django import forms

class EnvioMail(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Nombre'}))
    apellido = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Apellido'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}))
    mensaje = forms.CharField( required=True,widget=forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Mensaje','rows' : '5'}))
