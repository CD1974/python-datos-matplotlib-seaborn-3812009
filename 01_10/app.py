import matplotlib.pyplot as plt
import pandas as pd

df_gastos = pd.DataFrame({
        "categorías": ["Comida", "Vivienda", "Transporte", "Ropa", "Ahorro", "Otros"],
        "gastos": [170, 280, 120, 100, 110, 220],
    })

fig, ax = plt.subplots()

ax.pie(
    labels=df_gastos["categorías"], 
    x=df_gastos["gastos"],
    startangle=90,
    autopct="%1.1f%%",
)

ax.set_title("Gastos mensuales", fontsize=16, color='olivedrab', fontweight='bold')
plt.show()