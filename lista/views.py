from django.shortcuts import render
from .models import ListaDosFilmes

# Create your views here.


def index(request):
    filmes = ListaDosFilmes.objects.all()
    return render(request, 'lista/index.html', {
        'filmes': filmes
    })


def ver_filme(request, filme_id):
    filme = ListaDosFilmes.objects.get(id=filme_id)
    return render(request, 'lista/ver_filme.html', {
        'filme': filme
    })
