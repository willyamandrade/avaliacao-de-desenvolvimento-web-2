from django.shortcuts import render
from .forms import CadastroForm
from django.http import HttpResponse

viagens = []

# Create your views here.

def index(request):
    return render(request, 'planviagem/index.html', {'viagens' : viagens})

def cadastro(request):
    global viagens

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            destino = form.cleaned_data['destino']
            transporte = form.cleaned_data['transporte']

            viagens.append({"destino" : destino, "transporte" : transporte})
    else:
        form = CadastroForm()

    return render(request, 'planviagem/cadastro.html', {'form' : form})