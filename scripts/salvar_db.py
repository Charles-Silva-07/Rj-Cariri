import pandas as pd
from tqdm import tqdm

from django.db.models import Q
from rjcariri.base.models import Tabela


def run():
    """Ler a planilha"""
    plan = pd.read_excel("vendas.xlsx")

    number_of_rows = plan.shape[0]

    for i in tqdm(range(number_of_rows)):
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
