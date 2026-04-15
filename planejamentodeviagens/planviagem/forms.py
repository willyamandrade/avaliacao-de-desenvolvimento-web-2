from django import forms

class CadastroForm(forms.Form):
    destino = forms.CharField(label='Destino')
    transporte = forms.CharField(label='Transporte')