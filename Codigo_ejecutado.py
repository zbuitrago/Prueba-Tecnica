import pandas as pd
pd.set_option('precision', 3)

# carga de Base de datos
appsDf=pd.read_csv('googleplaystore5.csv')
userReviewDf=pd.read_csv('googleplaystore_user_reviews.csv')
# Limpiando base de googleplaystore de datos duplicados
cleanedAppsDf = appsDf.drop_duplicates(subset="App")

# Tipo de datos por Columna
cleanedAppsDf.dtypes 

# segundo punto 
##2.	¿Cuál es la variable con mayor cantidad de valores faltantes en cada una de las bases de datos?
print ("Total de Valores Faltantes en Apps")
print (cleanedAppsDf.isnull().sum())
print ("Total de Valores Faltantes en User Review")
print (userReviewDf.isnull().sum())

# Sexto punto
## ¿Cuáles son las categorías de aplicaciones con los promedios de ratings más altos?
print(cleanedAppsDf.groupby(['Category']).mean().sort_values(by='Rating',ascending=False))

# Octavo punto
## 8.	De las aplicaciones con más de 100k instalaciones ¿cuál es la que tiene mayor número de reviews positivos?
print (userReviewDf.groupby('App')['Sentiment'].value_counts().sort_values(ascending=False))
## continuacion octavo punto
print((cleanedAppsDf.loc[cleanedAppsDf['App'] == 'Helix Jump']))