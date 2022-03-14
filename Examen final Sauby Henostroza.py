import pandas as pd
import numpy as np
# Crea una Serie de los numeros 10, 20 and 10.
s1 = pd.Series([10,20,10])
s1

# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
s2 = pd.Series(['rojo', 'verde', 'azul'])
s2
# Crea un dataframe vacío llamado 'df'
df = pd.DataFrame()

# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
df = df.assign(numeros=pd.Series(s1).values)
df

# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
df = df.assign(Colores=pd.Series(s2).values)
df

# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"
import os
ruta = os.getcwd()
file_path = os.path.join(ruta,'/.avengers.csv')
df = pd.read_csv(file_path)
df 

# Muestra las primeras 5 filas del DataFrame.
df.head()

# Muestra las primeras 10 filas del DataFrame. 
df.head(n=10)

# Muestra las últimas 5 filas del DataFrame.
df.tail()

# Muestra el tamaño del DataFrame
df.size

# Muestra los data types del dataframe
df.dtypes

# Cambia el indice a la columna "fecha_inicio".
df = df.set_index("fecha_inicio")
df.index

# Ordena el índice de forma descendiente
df.sort_index(ascending = False)

# Resetea el índice
df.reset_index(drop=True, inplace=True)
df.index
#-------------------------------------------------------------------------------------

import pandas as pd
df_airbnb = pd.read_csv("./src/pandas/airbnb.csv")
df_airbnb
df_airbnb.dtypes

#Caso 1
condicion = (df_airbnb['reviews'] >10)  &  (df_airbnb['overall_satisfaction'] >4) &  (df_airbnb['accommodates'] ==4) &  (df_airbnb['bedrooms'] ==2)
df_airbnb=df_airbnb[condicion]
df_sorted= df_airbnb.sort_values(by=["overall_satisfaction","reviews"], ascending=[False, False])
df_sorted.head(n=3)

#Caso 2
import os
ruta = os.getcwd()
file_path = os.path.join(ruta,'./roberto.xls')
condicion = (df_airbnb['room_id'] ==97503) | (df_airbnb['room_id'] ==90387)   
df_Roberto=df_airbnb[condicion]
df_Roberto.to_excel(file_path,index=False)

#Caso 3
condicion = (df_airbnb['price'] <=50)   &  (df_airbnb['room_type'] =="Shared room") | (df_airbnb['room_type'] =="Shared room")
df_Diana=df_airbnb[condicion]
df_sort= df_Diana.sort_values(by=["price","overall_satisfaction"], ascending=[True,False])
df_sort.head(n=10)

##MatPlot
import matplotlib.pyplot as plt
df_airbnb.room_type.value_counts().plot.pie()