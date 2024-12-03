# Responsável por renderizar a página de galeria
from django.shortcuts import render
from django.http import HttpResponse

# aponta para a página principal
def index(request):
    return render(request, 'galeria/index.html')

# aponta para a página de imagem
def imagem(request):
    return render(request, 'galeria/imagem.html')