# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv')

grafico_gasolina = sns.lineplot(x='dia',y='venda',data=gasolina_df)
grafico_gasolina.set(xlabel='Dias', ylabel='Média de Vendas de Gasolina')
grafico_gasolina.figure.savefig('gasolina.png')