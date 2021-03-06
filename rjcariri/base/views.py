from django.shortcuts import render
from rjcariri.base.models import Tabela
from collections import defaultdict


def login(request):
    return render(request, 'registration/login.html')


def painel(request):
    return render(request, 'base/painel.html')


def Threebond(request):
    threebond = Tabela.objects.filter(Secao='THREEBOND')
    quantidade_por_semana = defaultdict(int)
    for row in threebond:
        quantidade_por_semana[row.Semana] += row.Quantidade

    return render(request, 'base/Threebond.html', context={'threebond': threebond,
                                                           'quantidade_por_semana': dict(quantidade_por_semana)})
