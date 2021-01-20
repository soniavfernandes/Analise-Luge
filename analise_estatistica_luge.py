# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:29:45 2020

"""
# Importar bibliotecas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def column_velocity(dataframe):
    velocity = []
    lista_tempos = dataframe['finish_time_seconds'].tolist()
    for i in range(len(lista_tempos)):
        # Pista = 1500 metros
        value = 1500/lista_tempos[i]
        velocity.append(value)
    return velocity
    

# ||||Cagorização do dataset||||
# Criar dataframes a partir dos ficheiros csv

atletas = pd.read_csv("athletes.csv")
jogos = pd.read_csv("sport_events.csv")

print("\nOutput:")
print(atletas.head())
print("\n")
print(jogos.head())

# Informação sobre as tabelas (#colunas, #linhas, tipo de dados)
print("\nOutput:")
print("Colunas DataFrame atletas:", atletas.columns)
print("Colunas DataFrame jogos:", jogos.columns)

# juntar as tabelas inner-join através de da coluna athlete_id
jogos_olimpicos = pd.merge(left=jogos, right=atletas, left_on="athlete_id", right_on="athlete_id")
print("\nOutput:")
print(jogos_olimpicos.head())

print("\nOutput:")
print("Colunas DataFrame jogos_olimpicos:", jogos_olimpicos.columns)

# Informação sobre as tabelas (#colunas, #linhas, tipo de dados)
print("\nOutput:")
print(jogos_olimpicos.info())

# Correção de tipos de dados
# objectos/integers => categorias
jogos_olimpicos.year = jogos_olimpicos.year.astype("category")
jogos_olimpicos.athlete_id = jogos_olimpicos.athlete_id.astype("category")
jogos_olimpicos.round_id = jogos_olimpicos.round_id.astype("category")
jogos_olimpicos.rank_id = jogos_olimpicos.rank_id.astype("category")
jogos_olimpicos.athlete_name = jogos_olimpicos.athlete_name.astype("category")
jogos_olimpicos.date_of_birth = jogos_olimpicos.date_of_birth.astype("category")
jogos_olimpicos.country_sport_id = jogos_olimpicos.country_sport_id.astype("category")

# Informação sobre as tabelas (#colunas, #linhas, tipo de dados)
print("\nOutput:")
print(jogos_olimpicos.info())

# Informação sobre geral estatítica
print("\nOutput:")
print(jogos_olimpicos.describe())

# Informação sobre geral estatítica
print("\nOutput:")
print(jogos_olimpicos.isna().sum())


# ||||Manipulação dos dados||||


velocidades_lista = column_velocity(jogos_olimpicos)
jogos_olimpicos['velocity (m/s)'] = velocidades_lista

print("\nOutput:")
print(jogos_olimpicos.head())

#Dataframes 2002    
round1_2002 = jogos_olimpicos[(jogos_olimpicos.year == 2002)&(jogos_olimpicos.round_id == "round 1")]
        
#Dataframes 2006
round1_2006 = jogos_olimpicos[(jogos_olimpicos.year == 2006)&(jogos_olimpicos.round_id == "round 1")]

#Dataframes 2010
round1_2010 = jogos_olimpicos[(jogos_olimpicos.year == 2010)&(jogos_olimpicos.round_id == "round 1")]

#Dataframes 2014
round1_2014 = jogos_olimpicos[(jogos_olimpicos.year == 2014)&(jogos_olimpicos.round_id == "round 1")]

#Dataframes 2018
round1_2018 = jogos_olimpicos[(jogos_olimpicos.year == 2018)&(jogos_olimpicos.round_id == "round 1")]

# E.g Visualização de uma das sub-dataframes
print("\nOutput:")
print(round1_2018.head())

# Criação de um dicionário de contagem de atletas qe participaram no evento
nr_atletas_ano_dic = {'2002': len(round1_2002['athlete_id'].unique().tolist()),\
        '2006': len(round1_2006['athlete_id'].unique().tolist()),\
        '2010': len(round1_2010['athlete_id'].unique().tolist()),\
        '2014': len(round1_2014['athlete_id'].unique().tolist()),\
        '2018': len(round1_2018['athlete_id'].unique().tolist())}

print("\nOutput:")
print(nr_atletas_ano_dic)

# Representação gráfica da Contagem dos atletas
plt.figure(figsize=(20,3))
plt.title('Contagem atletas nos diferentes eventos')
plt.bar(range(len(nr_atletas_ano_dic)),list(nr_atletas_ano_dic.values()),\
        tick_label=list(nr_atletas_ano_dic.keys()))

print("\nOutput:")
plt.show()
plt.savefig('contagem_atletas_anos.png')

# Filtragem da dataframe original para contagem da participação de cada um dos atletas nos eventos
print("\nOutput:")
print(jogos_olimpicos['athlete_name'].value_counts()/4)

# Criação do dicionário e conversão em dataframe de participações
participacoes_dic = {'Nº participações': jogos_olimpicos['athlete_name'].value_counts()/4}

participacoes = pd.DataFrame(participacoes_dic)

# Reprensentação gráfica da frequência de participações
print("\nOutput:")
participacoes.plot.hist(figsize=(15,3),title='Frequência de participações',alpha=0.5, xticks=np.arange(1, 5, step=1))
plt.savefig('frequencia_participaçoes.png')

# Criação de dicionário de conversão em dataframe da contagem dos atletas de cada país por cada ano
atletas_paises_ano_dic = {'2002': round1_2002['country_sport_id'].value_counts(),\
        '2006': round1_2006['country_sport_id'].value_counts(),\
        '2010': round1_2010['country_sport_id'].value_counts(),\
        '2014': round1_2014['country_sport_id'].value_counts(),\
        '2018': round1_2018['country_sport_id'].value_counts()}

atletas_paises_ano = pd.DataFrame(atletas_paises_ano_dic)

print("\nOutput:")
print(atletas_paises_ano)

# Representação gráfica da contagem agrupada de atletas de cada país que participaram nos diferentes eventos
print("\nOutput:")
atletas_paises_ano.plot.bar(figsize=(20,5), title='Contagem agrupada de atletas de cada país que participaram nos diferentes eventos')
plt.savefig('contagem_atletas_paises_anos_agrupados.png')

# Representação gráfica da contagem diferenciada de atletas de cada país que participaram nos diferentes eventos
print("\nOutput:")
figura_atletas_sub = atletas_paises_ano.plot.bar(subplots=True, figsize=(20,10), title='Contagem diferenciada de atletas de cada país que participaram nos diferentes eventos')
figura_atletas_sub[1].legend(loc=2)
plt.savefig('contagem_atletas_paises_anos.png')

# Agrupamento dos valores de ano e corrida com o tempo gasto de corrida
atletas_ano_tempo_medio = jogos_olimpicos.groupby(by=["year", "round_id"])["finish_time_seconds"].mean()
print("\nOutput:")
print(atletas_ano_tempo_medio)

# Representação gráfica dos valores grupamento dos valores de tempos de corridas entre anos
atletas_ano_tempo_medio.unstack().plot(kind='pie', subplots=True, figsize=(25,5), title='Acumulado de tempos de corridas entre anos')
plt.savefig('tempos_corridas_anos.png')

# Agrupamento dos valores de ano e corrida com a velocidade da corrida
atletas_ano_velocidade_media = jogos_olimpicos.groupby(by=["year", "round_id"])["velocity (m/s)"].mean()
print("\nOutput:")
print(atletas_ano_velocidade_media)

# Representação gráfica dos valores de velocidades entre diferentes anos - visulização gráfica não sobreposta
atletas_ano_velocidade_media.unstack().plot(kind='barh', figsize=(25,5), title='Acumulado de velocidades entre anos')
plt.savefig('velocidade_corridas_anos_barh.png')

# Representação gráfica dos valores de velocidades entre diferentes anos - visulização gráfica sobreposta
atletas_ano_velocidade_media.unstack().plot(kind='line', figsize=(25,5), title='Acumulado de velocidades entre anos')
plt.savefig('velocidade_corridas_anos_line.png')

