from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('<int:filme_id>', views.ver_filme, name='ver_filme'),

]
