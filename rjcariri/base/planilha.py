# from openpyxl import load_workbook
# from collections import defaultdict
#
# import os
# import django
#
#
# def lendo_excel(path_file):
#     wb = load_workbook(path_file)
#
#     abas = wb.sheetnames
#
#     print(f'Abas disponiveis no excel {abas}')
#
#     aba = wb['Página1']
#
#     linhas, colunas = aba.max_row, aba.max_column
#     nome_colunas = [ aba.cell(row=1, column=j).value for j in range(1, colunas + 1)]
#
#     tabela = defaultdict(list)
#     for lin in range(2, linhas + 1):
#         for col, nome_col in enumerate(nome_colunas, start=1):
#             tabela[nome_col].append(aba.cell(row=lin, column=col).value)
#
#     tabela = dict(tabela)
#
#     print(f'Nome da aba: {abas[0]}')
#     print(f'Número de linhas: {linhas}')
#     print(f'Número de colunas: {colunas}')
#
#     print(f'Nome das colunas: {nome_colunas}')
#
#     print(f'Valores {tabela}')
#
#     return dict(tabela)
#
#
# def salvando_no_banco(tabela):
#     from excel2db.core.models import Tabela
#
#     nomes = tabela['Nome']
#     saldos = tabela['Saldo']
#     for n, s in zip(nomes, saldos):
#         entrada = Tabela(nome=n, saldo=s)
#         entrada.save()
#
#
#
# if __name__ == '__main__':
#
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'excel2db.settings')
#     django.setup()
#
#     tabela = lendo_excel('Planilha.xlsx')
#     salvando_no_banco(tabela)