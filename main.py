import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from scipy import stats
import seaborn as sns
import re
from clean import *
from collections import Counter
movies = pd.read_csv('movies.csv', encoding='latin1', engine='python')
#pd.set_option('display.max_columns',None)

#Primeras filas con head
print("Exploracion de primeros datos de cada variable")
print(movies.head())

#Observaciones y variables
print("Numero de observaciones y variables")
print(movies.shape)

#Resumen de variables
print("Resumen de variables")
print(movies.describe().transpose())

#Evaluacion de normalidad de datos
quantitative_vars = ['popularity', 'budget', 'revenue', 'genresAmount', 'productionCoAmount',
'productionCountriesAmount', 'voteCount', 'voteAvg', 'actorsPopularity',
'actorsAmount', 'castWomenAmount', 'castMenAmount']
quantitative_vars_clean = ['actorsPopularity', 'castWomenAmount', 'castMenAmount']

for var in quantitative_vars:
    print("Evaluacion de normalidad de ", movies[var])
    if var in quantitative_vars_clean:
        data = clean_numeric_data(movies[var], var != 'actorsPopularity')["Item"].dropna()
    else:
        data = movies[var]
    print(type(data))
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

#Frecuencia de datos cualitativos
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


#Ejercicio 4

#4.1
print(movies.sort_values(by='budget',ascending=False)[['originalTitle','budget']].head(10))

#4.2
print(movies.sort_values(by='revenue',ascending=False)[['originalTitle','revenue']].head(10))

#4.3
print(movies.sort_values(by='voteCount',ascending=False)[['originalTitle','voteCount']].head(1))

#4.4
print(movies.sort_values(by='voteAvg',ascending=True)[['originalTitle','voteAvg']].head(1))

#4.5
print(movies['releaseDate'].str.split('-').str[0].value_counts().sort_values(ascending=False))

plt.bar(movies['releaseDate'].str.split('-').str[0].value_counts().sort_index().dropna().index,movies['releaseDate'].str.split('-').str[0].value_counts().sort_index().values,color='red')
plt.title('Grafico de barras para peliculas por año')
plt.xlabel('año')
plt.xticks(rotation=90)
plt.ylabel('Cantidad de peliculas')
plt.tight_layout()
plt.show()

#Extra

#4.16
#Peliculas con menos ingresos
#print(movies.sort_values(by='revenue',ascending=True)[['originalTitle','revenue']].head(5))

#4.17
#Director con mas peliculas hechas
print(movies['director'].value_counts().sort_values(ascending=False).head(1))