import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_empleados = pd.read_csv('empleados.csv', delimiter=";")

sns.set_theme(style="whitegrid")
g =  sns.jointplot(x="Experiencia", y="Salario", data=df_empleados, kind="reg", height=7)

g.set_axis_labels("Experiencia (años)", "Salario (Dólares)", fontsize=12)
plt.subplots_adjust(top=0.9) 
plt.suptitle("Relación entre Experiencia y Salario", fontsize=16, color='green', fontweight='bold', ha='center')
plt.tight_layout() 
plt.show()