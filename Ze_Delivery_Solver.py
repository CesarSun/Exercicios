import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


"""
Leitura Do Arquivo
"""

arquivo = 'C:\\Users\\CesarPC\\Desktop\\PC2\\20220318 ZeDelivery\\2 - Arquivo Tratado\\Ze Delivery Novo.xlsx'
ze_original = pd.read_excel(arquivo)
ze_original.columns = ze_original.columns.str.replace(' ', '_')
print(ze_original.columns)

"""
1.0 Limpeza Do Arquivo Em Uma Variável Nova
"""


# 1.1 Retirando colunas desnecessárias

ze_analise = ze_original.copy()
ze_analise.drop(['Payment_Method', 'Reasons', 'Shipping_Type', 'Order_Number'], axis=1, inplace=True)

# 1.2 Criando outros DataFrame para limpar mais o original

ze_rating_maiorq1 = ze_analise.loc[ze_analise.Rating >= 0, :].copy()

ze_comentarios = ze_analise[-ze_analise['Comment'].isna()].copy()

ze_analise.drop(['Comment', 'User', 'Date_&_Time'], axis=1, inplace=True)

print(ze_analise.columns)
# print(ze_analise.head(20))

"""
2.0 Criando Agrupamentos e Fazendo Uma Primeira Analise
"""

# 2.1 Cruzamento de Tabela

# print(pd.crosstab(ze_analise.Week, ze_analise.Rating)) # Identificação de notas -1 inseridas no DF no período que começou a dar problemas

ze_analise_rating_maiorq1 = ze_analise.loc[ze_analise.Rating >= 0, :].copy()

#print(pd.crosstab(ze_analise_rating_maiorq1.Week, ze_analise_rating_maiorq1.Rating))

# print(pd.crosstab(ze_analise.POC_ID, ze_analise.Rating))
# print(pd.crosstab(ze_analise_rating_maiorq1.POC_ID, ze_analise_rating_maiorq1.Rating))

# print(pd.crosstab(ze_analise.State, ze_analise.Rating))
# print(pd.crosstab(ze_analise_rating_maiorq1.State, ze_analise_rating_maiorq1.Rating))


# 2.2 Agrupamentos

# print(ze_analise.groupby('Week').Rating.mean())
# print(ze_analise_rating_maiorq1.groupby('Week').Rating.mean())
print(ze_analise.groupby('Week').Order_ID.count())

# print(ze_analise.groupby('POC_ID').Rating.mean())
# print(ze_analise_rating_maiorq1.groupby('POC_ID').Rating.mean())

# print(ze_analise.groupby('State').Rating.mean())
# print(ze_analise_rating_maiorq1.groupby('State').Rating.mean())


# 2.3 Mapa de Calor

#sb.heatmap(pd.crosstab(ze_analise_rating_maiorq1.POC_ID, ze_analise_rating_maiorq1.Week))

#sb.heatmap(pd.crosstab(ze_analise_rating_maiorq1.Week, ze_analise_rating_maiorq1.Rating))

#plt.show()

#sb.heatmap(ze_analise.drop(['State'], axis=1))
#plt.show()


"""

c1 = ze_analise.groupby('Week').Rating.mean()
c2 = ze_rating_maiorq1.groupby('Week').Rating.mean()

#print(pd.crosstab(ze_original.Week, ze_original.Rating))

comparacao1 = pd.DataFrame([c1, c2]).transpose()
#print(comparacao1)

ze_data = ze_analise['Date_&_Time']
lista = []
for d in ze_data:
    mes = d.month_name()
    lista.append(mes)
ze_analise['Mes'] = lista

ze_rating_maiorq1 = ze_analise.loc[ze_analise.Rating >= 0, :]

c3 = ze_analise.groupby('Mes').Rating.mean()
c4 = ze_rating_maiorq1.groupby('Mes').Rating.mean()

comparacao2 = pd.DataFrame([c3, c4]).transpose()
#print(comparacao2)


eixox = ze_analise['Week'].unique()

"""

"""

print(eixox, c1)
width = 0.25


plt.bar(eixox + width, c1, color='gold', width=width, edgecolor='black', label='Original')
plt.bar(eixox - width, c2, color='silver', width=width, edgecolor='black', label='Filtrado')
plt.xticks(eixox, eixox, rotation=90)
plt.xlabel("Weeks")
plt.ylabel("Rating")
plt.title("Comparação de Notas")

plt.annotate("Início da Distorção", xy=(28, 3.5), xycoords='data', xytext=(10, 5), textcoords='data',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
             c="green")

plt.legend()
plt.show()
"""