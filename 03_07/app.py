import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_empleados = pd.read_csv('empleados.csv', delimiter=";")
fig, axes = plt.subplots(2,2, figsize=(10, 8))

axes[0,0].hist(df_empleados['Edad'], bins=10, color='coral', edgecolor='black')
axes[0,0].set_ylabel('Frecuencia')
axes[0,0].set_xlabel('Edad')
axes[0,0].set_title('Distribución de Edades')

experiencia = df_empleados['Experiencia'].value_counts()
axes[0,1].bar(experiencia.index, experiencia.values, color='burlywood')
axes[0,1].set_ylabel('Cantidad')
axes[0,1].set_xlabel('Experiencia (Años)')
axes[0,1].set_title('Experiencia de Colaboradores')


axes[1,0].scatter(df_empleados['Experiencia'],df_empleados['Salario'], color='steelblue')
axes[1,0].set_ylabel('Salario')
axes[1,0].set_xlabel('Experiencia (Años)')
axes[1,0].set_title('Experiencia vs Salario')

departamento = df_empleados['Departamento'].value_counts()
axes[1,1].pie(
        list(departamento.values),
        labels=list(departamento.index),  
        autopct='%1.1f%%', 
        startangle=140, 
        colors=plt.cm.Paired.colors
    )
axes[1,1].set_title('Departamentos')

fig.suptitle('Información de los Colaboradores', fontsize=16, color='green', fontweight='bold', ha='center')
fig.tight_layout() 
plt.show()