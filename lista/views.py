from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import ListaDosFilmes
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    filmes = ListaDosFilmes.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(filmes, 10)

    page = request.GET.get('p')
    filmes = paginator.get_page(page)

    return render(request, 'lista/index.html', {
        'filmes': filmes
    })


def ver_filme(request, filme_id):
    filme = get_object_or_404(ListaDosFilmes, id=filme_id)

    if not filme.mostrar:
        raise Http404
    return render(request, 'lista/ver_filme.html', {
        'filme': filme
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        raise Http404()
    campos = Concat('nome', Value(' '), 'direcao')

    filmes = ListaDosFilmes.objects.annotate(
        nome_e_direcao=campos
    ).filter(
        Q(nome_e_direcao__icontains=termo) | Q(genero__icontains=termo)
    )
    paginator = Paginator(filmes, 10)

    page = request.GET.get('p')
    filmes = paginator.get_page(page)

    return render(request, 'lista/busca.html', {
        'filmes': filmes
    })

