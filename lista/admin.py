from django.contrib import admin
from .models import Categoria, ListaDosFilmes

# Register your models here.


class ListaDeFilmesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'direcao', 'ano', 'genero', 'categoria', 'data_criacao')
    list_display_links = ('nome', 'direcao')
    list_filter = ('direcao', 'ano')
    list_per_page = 10
    search_fields = ('nome', 'direcao', 'ano')


admin.site.register(Categoria)
admin.site.register(ListaDosFilmes, ListaDeFilmesAdmin)
