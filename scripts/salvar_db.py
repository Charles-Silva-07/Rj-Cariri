import pandas as pd
import os
import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rjcariri.settings')
# django.setup()
from django.db.models import Q  # noqa
from rjcariri.base.models import Tabela  # noqa


def run():
    """Ler a planilha"""
    plan = pd.read_excel("vendas.xlsx")

    for i in range(plan.shape[0]):
        ano = plan.loc[i, "ano"]
        mes = plan.loc[i, "mes"]
        semana = plan.loc[i, "semana"]
        secao = plan.loc[i, "secao"]
        produto = plan.loc[i, "produto"]
        descricao = plan.loc[i, "descricao"]
        quantidade = plan.loc[i, "quantidade"]
        faturamento = plan.loc[i, "faturamento"]
        positivacao = plan.loc[i, "positivacao"]
        cobertura = plan.loc[i, "cobertura"]
        regiao = plan.loc[i, "regiao"]

        criterion1 = Q(semana=semana)
        criterion2 = Q(produto=produto)

        if Tabela.objects.filter(criterion1 & criterion2).count() == 0:
            t = Tabela(ano=ano, mes=mes, semana=semana, secao=secao, produto=produto, descricao=descricao,
                       quantidade=quantidade,
                       faturamento=faturamento, positivacao=positivacao, cobertura=cobertura, regiao=regiao)

            t.save()