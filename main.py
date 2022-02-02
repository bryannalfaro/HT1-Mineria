import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from scipy import stats
import seaborn as sns
import re
from clean import *
from collections import Counter
movies = pd.read_csv('movies.csv')
#pd.set_option('display.max_columns',None)

'''#Primeras filas con head
print("Exploracion de primeros datos de cada variable")
print(movies.head())

#Observaciones y variables
print("Numero de observaciones y variables")
print(movies.shape)

#Resumen de variables
print("Resumen de variables")
print(movies.describe().transpose())

#Evaluacion de normalidad de datos
data = movies['popularity'].dropna()
plt.hist(data,color='green')
plt.title('Histograma para popularidad')
plt.xlabel('Popularidad')
plt.ylabel('Cantidad')
plt.show()
qqplot(data , line='s')
plt.show()

print('Curtosis: ',stats.kurtosis(data))
print('Asimetria: ',stats.skew(data))

data = movies['budget'].dropna()
plt.hist(data,color='green')
plt.title('Histograma para budget')
plt.xlabel('Budget')
plt.ylabel('Cantidad')
plt.show()
qqplot(data , line='s')
plt.show()

print('Curtosis: ',stats.kurtosis(data))
print('Asimetria: ',stats.skew(data))

data = movies['revenue'].dropna()
plt.hist(data,color='green')
plt.title('Histograma para revenue')
plt.xlabel('Revenue')
plt.ylabel('Cantidad')
plt.show()
qqplot(data , line='s')
plt.show()

print('Curtosis: ',stats.kurtosis(data))
print('Asimetria: ',stats.skew(data))

data = movies['genresAmount'].dropna()
plt.hist(data,color='green')
plt.title('Histograma para genresAmount')
plt.xlabel('genresAmount')
plt.ylabel('Cantidad')
plt.show()
qqplot(data , line='s')
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
print(movies.sort_values(by='voteAvg',ascending=True)[['title','voteAvg']].head(1))

#4.5
print(movies['releaseDate'].str.split('-').str[0].value_counts().sort_values(ascending=False))

plt.bar(movies['releaseDate'].str.split('-').str[0].value_counts().sort_index().dropna().index,movies['releaseDate'].str.split('-').str[0].value_counts().sort_index().values,color='red')
plt.title('Grafico de barras para peliculas por año')
plt.xlabel('año')
plt.xticks(rotation=90)
plt.ylabel('Cantidad de peliculas')
plt.tight_layout()
plt.show()'''

#Extra

#4.16
#Peliculas con menos ingresos
#print(movies.sort_values(by='revenue',ascending=True)[['originalTitle','revenue']].head(5))

#4.17
#Director con mas peliculas hechas
print(movies['director'].value_counts().sort_values(ascending=False).head(1))