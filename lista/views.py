from django.shortcuts import render, get_object_or_404
from .models import ListaDosFilmes
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    filmes = ListaDosFilmes.objects.all()
    paginator = Paginator(filmes, 10)

    page = request.GET.get('p')
    filmes = paginator.get_page(page)

    return render(request, 'lista/index.html', {
        'filmes': filmes
    })


def ver_filme(request, filme_id):
    filme = get_object_or_404(ListaDosFilmes, id=filme_id)
    return render(request, 'lista/ver_filme.html', {
        'filme': filme
    })
