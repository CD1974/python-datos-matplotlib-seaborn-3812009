import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_empleados = pd.read_csv('empleados.csv', delimiter=";")

sns.set_theme(style="whitegrid")
sns.pairplot(df_empleados, 
             plot_kws={'color': '#ff7f0e'},
             diag_kws={'color': '#bcbd22'})
plt.show()