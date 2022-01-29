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
print((movies['originalTitle'].value_counts()))
print((movies['originalTitle'].value_counts()))
print((movies['originalTitle'].value_counts()))
print((movies['originalTitle'].value_counts()))
print((movies['originalTitle'].value_counts()))
print((movies['originalTitle'].value_counts()))
