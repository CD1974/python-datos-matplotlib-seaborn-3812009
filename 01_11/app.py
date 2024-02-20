import matplotlib.pyplot as plt
import pandas as pd


df_ventas = pd.DataFrame({
    'cromos': ['Cromo 101', 'Cromo 102', 'Cromo 103'],
    'ventas': [100, 150, 200]
  })

fig, ax = plt.subplots()

ax.bar(df_ventas['cromos'], df_ventas['ventas'], color=['saddlebrown', 'rosybrown', 'gray'])
ax.set_xlabel('Productos')
ax.set_ylabel('Venta (Dólares)')

ax.set_title("Ventas de cromos en el tercer trimestre de 2023", fontsize=16, color='olivedrab', fontweight='bold', pad=20)
plt.show()