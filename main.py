import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from scipy import stats
import seaborn as sns
movies = pd.read_csv('movies.csv')
#pd.set_option('display.max_columns',None)

#Primeras filas con head
'''print("Exploracion de primeros datos de cada variable")
print(movies.head())

#Observaciones y variables
print("Numero de observaciones y variables")
print(movies.shape)

#Resumen de variables
print("Resumen de variables")
print(movies.describe().transpose())'''

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
