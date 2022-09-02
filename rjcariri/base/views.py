from django.shortcuts import render
from rjcariri.base.models import Tabela
from collections import defaultdict


def login(request):
    return render(request, 'registration/login.html')


def painel(request):
    return render(request, 'base/painel.html')


class Produto:
    def __init__(self, codigo, descricao, numero_semanas):
        self.codigo = codigo
        self.descricao = descricao
        self.numero_semanas = numero_semanas


def Threebond(request):

    threebond = Tabela.objects.filter(secao='THREEBOND')

    produtos = set()
    semanas = set()

    tabela = dict()
    total_quantidade_por_semana = defaultdict(int)
    descricao = defaultdict(list)

    for row in threebond:
        semanas.add(row.semana)
        produtos.add(row.produto)
        descricao[row.produto] = row.descricao
        total_quantidade_por_semana[row.semana] += row.quantidade

    for p in produtos:
        row = {
            'descricao': descricao[p],
            'semanas': {}
        }
        for i in range(1, len(semanas) + 1):
            row['semanas'][i] = '-'
        tabela[p] = row

    for p in produtos:
        for t in threebond:
            if t.produto == p:
                tabela[p]['semanas'][t.semana] = t.quantidade

    return render(request, 'base/Threebond.html', context={'tabela': tabela,
                                                           'total_quantidade_por_semana': dict(total_quantidade_por_semana)})
