import pandas as pd
import matplotlib.pyplot as plt

df_altura_peso = pd.read_csv("altura_peso.csv", delimiter=";")

etiquetas = [i + 1 for i in range(len(df_altura_peso['altura']))]

fig, ax = plt.subplots()
ax.bar(etiquetas, df_altura_peso['altura'], yerr=0.05, capsize=5, color='olivedrab')

ax.set_xlabel('Persona')
ax.set_ylabel('Altura(m)')
ax.set_title('Altura de personas con barras de error', color='olivedrab', fontweight='bold', pad=20)
plt.show()