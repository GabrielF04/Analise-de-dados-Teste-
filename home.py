from sys import displayhook

import pandas as pd


Excel = pd.read_excel('Compras.xlsx')

colunas_do_excel = ['ValorFinal', 'ValorUnitario', 'Quantidade']
dados = Excel[colunas_do_excel]

relatorio =  input("Você deseja receber o relatório diário? Se sim digite sim")

if relatorio == "Sim":
    print(Excel)

else:
    print()

print("Relatório diário:")

Faturamento = Excel['ValorFinal'].sum()
print("Esse é o faturamento total:", Faturamento)



Media = Excel['ValorUnitario'].median()
print("Essa é a média:",Media)


Quantidade_Vendida = Excel['Quantidade'].sum()
print("Essa é a quantidade vendida", Quantidade_Vendida)


Total_Gasto = Excel['ValorFinal'].sum()
print("O total gasto é de:", Total_Gasto)