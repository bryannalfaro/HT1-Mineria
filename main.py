from math import ceil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from scipy import stats
import seaborn as sns
import re
from clean import *
from collections import Counter
# movies = pd.read_csv('movies.csv', encoding='unicode_escape')
movies = pd.read_csv('movies.csv', encoding='latin1', engine='python')
#pd.set_option('display.max_columns',None)

'''
#Primeras filas con head
print("Exploracion de primeros datos de cada variable")
print(movies.head())

#Observaciones y variables
print("Numero de observaciones y variables")
print(movies.shape)

#Resumen de variables
print("Resumen de variables")
print(movies.describe().transpose())
'''

'''
#Evaluacion de normalidad de datos
quantitative_vars = ['popularity', 'budget', 'revenue', 'runtime', 'genresAmount', 'productionCoAmount',
'productionCountriesAmount', 'voteCount', 'voteAvg', 'actorsPopularity',
'actorsAmount', 'castWomenAmount', 'castMenAmount']
quantitative_vars_clean = ['actorsPopularity', 'castWomenAmount', 'castMenAmount']

for var in quantitative_vars:
    print("Evaluacion de normalidad de ", movies[var])
    if var in quantitative_vars_clean:
        data = clean_numeric_data(movies[var], var != 'actorsPopularity')["Item"].dropna()
    else:
        data = movies[var]
    plt.hist(data,color='green')
    plt.title(f'Histograma para {var}')
    plt.xlabel(var)
    plt.ylabel('Cantidad')
    plt.show()
    qqplot(data , line='s')
    plt.title(f'QQplot para {var}')
    plt.show()

    print('Curtosis: ',stats.kurtosis(data))
    print('Asimetria: ',stats.skew(data))
'''

#Frecuencia de datos cualitativos
'''
print((movies['id'].value_counts()))
print((movies['originalTitle'].value_counts()))
print((movies['originalLanguage'].value_counts()))
print((movies['title'].value_counts()))
print((movies['homePage'].value_counts()))
print((movies['video'].value_counts()))
print((movies['director'].value_counts()))
print((movies['genres'].value_counts()))
print((movies['productionCompany'].value_counts()))
print((movies['productionCompanyCountry'].value_counts()))
print((movies['productionCountry'].value_counts()))
print((movies['releaseDate'].value_counts()))
print((movies['actors'].value_counts()))
print((movies['actorsCharacter'].value_counts()))
'''

'''
#Evaluacion de datos sin estar agrupados
print("Genres")
print(clean_data(movies['genres']))
print("productionCompany")
print(clean_data(movies['productionCompany']))
print("productionCompanyCountry")
print(clean_data(movies['productionCompanyCountry']))
print("productionCountry")
print(clean_data(movies['productionCountry']))
print("actors")
print(clean_data(movies['actors']))
print("actorsCharacter")
print(clean_data(movies['actorsCharacter']))
'''

'''
cualitative_vars = ['id', 'originalTitle', 'originalLanguage', 'title', 'homePage', 'video', 'director', 'genres', 'productionCompany',
'productionCompanyCountry', 'productionCountry', 'releaseDate', 'actors', 'actorsCharacter']
cualitative_vars_clean = ['director', 'genres', 'productionCompany', 'productionCompanyCountry', 'productionCountry', 'director', 'actors', 'actorsCharacter']

for var in cualitative_vars:
    if var in cualitative_vars_clean:
        data = clean_data(movies[var])
    else:
        data = movies[var].value_counts()
    plt.figure(figsize=(15,5))
    if var in cualitative_vars_clean:
        sns.barplot(data["Item"].values, data["Count"].values, alpha=0.8)
    else:
        sns.barplot(data.index, data.values, alpha=0.8)
    plt.title(f'Frecuencia de datos cualitativos para {var}')
    plt.ylabel('Cantidad')
    plt.xlabel(var)
    plt.show()
'''

'''
#Ejercicio 4

#4.1
print(movies.sort_values(by='budget',ascending=False)[['originalTitle','budget']].head(10))

#4.2
print(movies.sort_values(by='revenue',ascending=False)[['originalTitle','revenue']].head(10))

#4.3
print(movies.sort_values(by='voteCount',ascending=False)[['originalTitle','voteCount']].head(1))

#4.4
print(movies.sort_values(by='voteAvg',ascending=True)[['title','voteAvg']].head(1))

#4.5
print(movies['releaseDate'].str.split('-').str[0].value_counts().sort_values(ascending=False))

plt.bar(movies['releaseDate'].str.split('-').str[0].value_counts().sort_index().dropna().index,movies['releaseDate'].str.split('-').str[0].value_counts().sort_index().values,color='red')
plt.title('Grafico de barras para peliculas por año')
plt.xlabel('año')
plt.xticks(rotation=90)
plt.ylabel('Cantidad de peliculas')
plt.tight_layout()
plt.show()
'''

'''
# 4.6
# Top 20 peliculas recientes y genero principal
recentMovies = movies.sort_values(by='releaseDate',ascending=False)[['originalTitle','genres']].head(20)
recentMovies["genres"] = recentMovies["genres"].str.split('|').str[0]
print(recentMovies)
principalGenres = movies["genres"].str.split('|').str[0].value_counts().sort_values(ascending=False)
print(principalGenres.head(1))
sns.barplot(principalGenres.index, principalGenres.values, alpha=0.8)
plt.title(f'Géneros principales más repetidos')
plt.ylabel('Cantidad')
plt.xlabel('Género')
plt.show()

# 4.7
# Top 20 peliculas con mayor ganancia y genero principal
mostRevenueMovies = movies.sort_values(by='revenue',ascending=False)[['originalTitle','genres']].head(20)
print(mostRevenueMovies["genres"].str.split('|').str[0].value_counts().sort_values(ascending=False).head(3))

# 4.8
# correlacion entre 'revenue' y 'actorsAmount'
moviesActorsAmountFilter = movies[movies['actorsAmount'] < 313]
print('Correlacion entre revenue y actorsAmount: ', moviesActorsAmountFilter.corr()['revenue']['actorsAmount'])
plt.scatter(moviesActorsAmountFilter['revenue'], moviesActorsAmountFilter['actorsAmount'])
plt.title('Correlación entre ganancias y cantidad de actores')
plt.xlabel('Ganancias')
plt.ylabel('Cantidad de actores')
plt.show()

# Peliculas de los ultimos 5 años
recentMovies = movies[movies['releaseDate'].str.split('-').str[0].astype(int) > 2022-5]
recentMovies = recentMovies[recentMovies['actorsAmount'] < 313]
recentMovies = recentMovies.sort_values(by='releaseDate',ascending=True)[['releaseDate','actorsAmount']]
# grafica lineal
plt.plot(recentMovies['releaseDate'], recentMovies['actorsAmount'])
plt.title('Cantidad de actores vs fecha de lanzamiento')
plt.xlabel('Fecha de lanzamiento')
plt.ylabel('Cantidad de actores')
plt.xticks(rotation=90)
plt.show()

# 4.9
# correlacion entre 'castMenAmount' y 'popularity'
moviesCastGenresFiltered = movies
moviesCastGenresFiltered["castMenAmount"] = clean_numeric_data(moviesCastGenresFiltered["castMenAmount"], True, 313, keep_size=True)["Item"]
print('Correlacion entre castMenAmount y popularity: ', moviesCastGenresFiltered.corr()['castMenAmount']['popularity'])
plt.scatter(moviesCastGenresFiltered['castMenAmount'], moviesCastGenresFiltered['popularity'])
plt.title('Correlación entre cantidad de actores masculinos y popularidad')
plt.xlabel('Cantidad de actores masculinos')
plt.ylabel('Popularidad')
plt.show()

# correlacion entre 'castWomenAmount' y 'popularity'
moviesCastGenresFiltered["castWomenAmount"] = clean_numeric_data(moviesCastGenresFiltered["castWomenAmount"], True, 313, keep_size=True)["Item"]
print('Correlacion entre castWomenAmount y popularity: ', moviesCastGenresFiltered.corr()['castWomenAmount']['popularity'])
plt.scatter(moviesCastGenresFiltered['castWomenAmount'], moviesCastGenresFiltered['popularity'])
plt.title('Correlación entre cantidad de actrices y popularidad')
plt.xlabel('Cantidad de actrices')
plt.ylabel('Popularidad')
plt.show()

# correlacion entre 'castMenAmount' y 'reveue'
print('Correlacion entre castMenAmount y revenue: ', moviesCastGenresFiltered.corr()['castMenAmount']['revenue'])
plt.scatter(moviesCastGenresFiltered['castMenAmount'], moviesCastGenresFiltered['revenue'])
plt.title('Correlación entre cantidad de actores masculinos y ganancias')
plt.xlabel('Cantidad de actores masculinos')
plt.ylabel('Ganancias')
plt.show()

# correlacion entre 'castWomenAmount' y 'reveue'
print('Correlacion entre castWomenAmount y revenue: ', moviesCastGenresFiltered.corr()['castWomenAmount']['revenue'])
plt.scatter(moviesCastGenresFiltered['castWomenAmount'], moviesCastGenresFiltered['revenue'])
plt.title('Correlación entre cantidad de actrices y ganancias')
plt.xlabel('Cantidad de actrices')
plt.ylabel('Ganancias')
plt.show()

# 4.10
# Top 20 peliculas mejor calificadas y directores
bestRatingMovies = movies.sort_values(by='voteAvg', ascending=False)[['originalTitle', 'voteAvg', 'director']].head(20)
print(bestRatingMovies)

# corr = movies.corr()
# # ax = sns.heatmap(corr, annot=True, fmt=".2f", cmap='Blues',
# #            vmin=-1, vmax=1, cbar_kws={"shrink": .8})

#4.11

# r, p = stats.pearsonr(movies['revenue'], movies['budget'])
# print(f"Correlacion Pearson r={r}, p={p}")

# fig, ax = plt.subplots(1, 1, figsize=(6,4))
# ax.scatter(x=movies.budget, y=movies.revenue, alpha= 0.8)
# ax.set_xlabel('Budget')
# ax.set_ylabel('Revenue');

# plt.show()

#4.12
# print('Correlación Pearson: ', movies['revenue'].corr(movies['releaseDate'].str.split('-').str[1].dropna().astype(int), method='pearson'))
# print('Correlación spearman: ', movies['revenue'].corr(movies['releaseDate'].str.split('-').str[1].dropna().astype(int), method='spearman'))
# print('Correlación kendall: ', movies['revenue'].corr(movies['releaseDate'].str.split('-').str[1].dropna().astype(int), method='kendall'))

# fig, ax = plt.subplots(1, 1, figsize=(6,4))
# ax.scatter(x=movies.revenue, y=movies['releaseDate'].str.split('-').str[1], alpha= 0.8)
# ax.set_xlabel('Reveneu')
# ax.set_ylabel('Release Date');

# plt.show()

#4.13
# movies.index = pd.to_datetime(movies['releaseDate'],yearfirst=True)
# print(movies.groupby(by=[movies.index.month]).agg({'revenue':'sum'}).sort_values(by= "revenue", ascending=False))


#4.14

# print('Correlación Pearson: ', movies['revenue'].corr(movies['voteAvg'], method='pearson'))
# print('Correlación spearman: ', movies['revenue'].corr(movies['voteAvg'], method='spearman'))
# print('Correlación kendall: ', movies['revenue'].corr(movies['voteAvgS'], method='kendall'))

# fig, ax = plt.subplots(1, 1, figsize=(6,4))
# ax.scatter(x=movies.revenue, y=movies.voteAvg, alpha= 0.8)
# ax.set_xlabel('Reveneu')
# ax.set_ylabel('Votes Average');

# plt.show()

#4.15
# print(movies.sort_values(by='runtime',ascending=False)[['genres','runtime']].head(4))
'''
'''
#Extra

#4.16
#Peliculas con menos ingresos
print(movies.sort_values(by='revenue',ascending=True)[['title','revenue']].head(5))

#4.17
#Director con mas peliculas hechas
# print(movies['director'].value_counts().sort_values(ascending=False).head(1))
print(movies['director'].value_counts().sort_values(ascending=False).head(1))

#4.18
#Pais de produccion de las 5 peliculas con mas ingreso
print(movies.sort_values(by='revenue',ascending=False)[['productionCountry','revenue']].head(5))

#4.19
#2 Companias con mayor cantidad de peliculas realizadas
print(movies['productionCompany'].value_counts().head(2))

#4.20
movies['mainProductionCountry'] = movies['productionCountry'].str.split('|').str[0]
print(movies.groupby('mainProductionCountry')['runtime'].mean().sort_values(ascending=False))

#4.21
#Peliculas con mayor cantidad de actores
print(movies.sort_values(by='actorsAmount',ascending=False)[['title','actorsAmount']].head(1))
'''
