# -*- coding: utf-8 -*-
"""[Jonatas-Liberato] Análise de Dados Meteorológicos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S1Ch8tl7tzkyy5kJNZlPbl-sCskgtabo

# **ANÁLISE DE DADOS METEOROLÓGICOS**

Mais um projeto para testar novas/já conhecidas habilidades. Neste script, faremos uma análise de dados meteorológicos de diversas cidades, usando um dataset com muitos registros e que está armazenado em nuvem, devido ao seu tamanho.

-- 

O referido dataset possui registros de vários países, desde 1995 até 2020.

-- 

**Dataset**: [AQUI](https://drive.google.com/file/d/1UOv8UARJZhJJ4Igzmok2HXYHzz0qRNy6/view?usp=sharing)

# Projeto
"""

# Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Dataset
from google.colab import drive
drive.mount('/content/drive')

dataset = pd.read_csv('/content/drive/MyDrive/_datasets/city_temperature.csv')
dataset

"""# Análise Exploratória"""

dataset.info()

dataset.shape

# Contando valores únicos
dataset.nunique()

dataset.head(3)

dataset['Region'].value_counts()

dataset['Country'].value_counts()

dataset.isnull().sum()

dataset['State'].isnull().sum()

dataset['Country'].value_counts()

dataset.describe()

# Filtrando pelo Brasil
df_brazil = dataset.loc[dataset['Country'] == 'Brazil']
df_brazil

"""Ao explorar os dados notamos:
- Existem mais de 1 milhão de registros NaN em Country
- A data já está separada por dia, mês e ano
- A temperatura média está em Fahrenheit e faremos uma transformação
- Alguns países possuem problemas com estados, pois o dataset só tem 52 estados

# Tratamento dos Dados

**Eliminando o state**
"""

dataset.drop('State', axis = 'columns', inplace = True)

dataset.head()

"""**Reorganizando os índices**"""

dataset.reset_index(inplace = True)

dataset.head()

"""**Eliminando a coluna do índice**"""

dataset.drop('index', axis = 1, inplace = True)

dataset.head()

"""**Indentificamos diversos temperaturas atípicas como -99.**"""

# Todos os registros -99
dataset.loc[dataset['AvgTemperature'] == -99]

"""**Então nomearemos estas como NaN.**"""

dataset.loc[dataset['AvgTemperature'] == -99] = np.nan

dataset.loc[dataset['AvgTemperature'] == -99]

"""**Verificando os valores missing**"""

dataset.isnull().sum()

"""**Eliminando os valores missing**"""

dataset.dropna(inplace = True)

dataset.isnull().sum()

"""**Convertendo manualmente a temperatura de Fahrenheit para Celsius**

**Fórmula: ºF to ºC: (ºF - 32) x 5/9 = ºC**
"""

# Convertendo
dataset['AvgCelsius'] = (dataset['AvgTemperature'] - 32) * 5/9

dataset.head()

"""**Deletando a coluna da Temperatura em Fahrenheit**"""

dataset.drop('AvgTemperature', axis = 1, inplace = True)

dataset.head()

"""# Temperatura Média Ao Longo do Tempo

**Construindo um gráfico para melhor visualização**
"""

plt.figure()
sns.lineplot(x = 'Year', y = 'AvgCelsius', data = dataset)
plt.show()

dataset[dataset['Year'] == 1999].shape

"""# Temperatura Média do Brasil Ao Longo do Tempo"""

ds_brazil = dataset.groupby(['Year', 'Month'])['AvgCelsius'].mean()

ds_brazil

"""# Desfazendo o Grupo de Informações"""

ds_brazil = ds_brazil.unstack()

"""**O dataset ficou: Meses em colunas e linhas as temperaturas**

**Visualizando graficamente**
"""

plt.figure(figsize = (10, 5))
sns.heatmap(data = ds_brazil, annot = True, cmap = 'coolwarm')
plt.show()

"""# Temperatura Média de Outras Cidades no Brasil"""

ds_city = dataset.groupby('City')['AvgCelsius'].mean()

ds_city = ds_city.to_frame().reset_index()

ds_city

plt.figure()
sns.lineplot(x = 'City', y = 'AvgCelsius', data = ds_city)
plt.show()

"""# Temperatura Média de São Paulo em Dezembro"""

dataset.head()

ds_saopaulo = dataset.loc[dataset['City'] == 'Sao Paulo']

ds_saopaulo

sp_december = ds_saopaulo.loc[ds_saopaulo['Month'] == 12]

sp_december

plt.figure()
sns.lineplot(x = 'Year', y = 'AvgCelsius', data = ds_city)
plt.show()

"""# Conclusão:

*Apesar do dataset possuir diversos valores inconsistentes, esse projeto simples seviu para trabalhar muito com filtros.*
"""

#Autor: Jonatas A. Liberato
#Ref: Eduardo Rocha