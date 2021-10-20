#importando biblioteca panda
import pandas as pd
import numpy as np

#coletando dados do arquivo csv
data = pd.read_csv('C:/Users/fastn/Desktop/KingHouse/repos/kc_house_data.csv')

#mostre as 5 primeiras linhas
print(data.head())

#mostre o numero de linhas e colunas do dataset
print(data.shape)

#mostre na tela o nome das colunas do dataset
print(data.columns)

#mostre na tela o cojunto de dados ordenado pela coluna price ordenados do maior pro menos
print(data[['id', 'price']].sort_values('price', ascending=False))

#mostre na tela a soma total de quartos do conjunto de dados
print(data[['bedrooms']].sum())

#mostre na tela Quantas casas possuem 2 banheiros
print(data[['bathrooms']].value_counts()[2.00])

#mostre na tela Qual o preço médio de todas as casas no conjunto de dados
print(np.round(data[['price']].mean(numeric_only=float), 2))

#mostre na tela o preço médio das casas com 2 banheiros
#print(np.round(data.loc[data['bathrooms'] == 2, 'price'].mean())  OU
print(data[['bathrooms', 'price']].query('bathrooms == 2').mean())

#mostre na tela Qual o preço mínimo entre as casas com 3 quartos
print(data[['bedrooms', 'price']].query('bedrooms == 3').min())

#mostre Quantas casas possuem mais de 300 metros quadrados na sala de estar
data['m2'] = data['sqft_living'] * 0.092     #convertendo metros pra pés
print(len(data.query('m2 > 300')))

#mostre Quantas casas tem mais de 2 andares
print(len(data.query('floors > 2')))

#mostre Quantas casas tem vista para o mar
print(len(data.query('waterfront == True')))

#mostre Das casas com vista para o mar, quantas tem 3 quartos
print(len(data.query('waterfront == True & bedrooms == 3')))

#mostre Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros
print(len(data.query('m2 > 300 & bathrooms >2')))
