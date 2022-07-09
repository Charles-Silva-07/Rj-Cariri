import pandas as pd
import os
import django
from django.db.models import Q
from rjcariri.base.models import Tabela


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rjcariri.settings')
django.setup()


"""Ler a planilha"""
plan = pd.read_excel("vendas.xlsx")

for i in range(plan.shape[0]):
    Ano = plan.loc[i, "Ano"]
    Semana = plan.loc[i, "Semana"]
    Secao = plan.loc[i, "Secao"]
    Produto = plan.loc[i, "Produto"]
    Descricao = plan.loc[i, "Descricao"]
    Quantidade = plan.loc[i, "Quantidade"]
    Faturamento = plan.loc[i, "Faturamento"]
    Positivacao = plan.loc[i, "Positivacao"]
    Cobertura = plan.loc[i, "Cobertura"]
    Regiao = plan.loc[i, "Regiao"]

    criterion1 = Q(Semana=Semana)
    criterion2 = Q(Produto=Produto)

    if Tabela.objects.filter(criterion1 & criterion2).count() == 0:
        t = Tabela(Ano=Ano, Semana=Semana, Secao=Secao, Produto=Produto, Descricao=Descricao, Quantidade=Quantidade,
                   Faturamento=Faturamento, Positivacao=Positivacao, Cobertura=Cobertura, Regiao=Regiao)

        t.save()
