import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Data.csv')

# x es la variable independiente y la y la dependeinte que sera comprado.
x = df.iloc[:, :-1].values #todas las columnas menos las ultimas
y = df.iloc[:, 3].values #solo la tercer columna
print(df)

#solucionar datos NaN


