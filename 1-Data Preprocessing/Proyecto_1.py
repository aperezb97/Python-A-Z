import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Data.csv')
df.head()
# x es la variable independiente y la y la dependeinte que sera comprado.
x = df.iloc[:, :-1].values #todas las columnas menos las ultimas
y = df.iloc[:, 3].values #solo la tercer columna



#solucionar datos NaN


 
