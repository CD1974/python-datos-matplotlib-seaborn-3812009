import pandas as pd
import matplotlib.pyplot as plt

df_temperaturas = pd.read_csv("temperaturas.csv", delimiter=";")

fig, ax = plt.subplots()

ax.hist(df_temperaturas['tmaxima'], bins=15, color='lightgray', edgecolor='black')

ax.set_xlabel('Temperatura (°C)')
ax.set_ylabel('Frecuencia')
ax.set_title('Temperaturas máximas diarias \n (Agosto - Setiembre 2023)', color='olivedrab', fontweight='bold', pad=5)
plt.show()
