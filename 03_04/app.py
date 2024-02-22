import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_empleados = pd.read_csv('empleados.csv', delimiter=";")

df_correlacion = df_empleados.corr()
f, ax = plt.subplots()

mask = np.triu(np.ones_like(df_correlacion, dtype=bool))

sns.heatmap(df_correlacion, 
            mask=mask, 
            annot=True, 
            center=0, 
            fmt=".2f",
            linewidths=.5, 
            cbar_kws={"shrink": .5}
        )

ax.set_title('Correlación entre edad, salario y experiencia', color='olivedrab', ha='center', fontweight='bold', pad=20)
plt.show()