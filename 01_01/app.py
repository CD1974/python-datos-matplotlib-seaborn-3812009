import matplotlib.pyplot as plt
import pandas as pd

df_ventas = pd.DataFrame({
        "annio": [2019, 2020, 2021, 2022, 2023, 2024],
        "venta_cromos_101": [119.25, 141.28, 132.06, 205.33, 216.59, 157.51],
        "venta_cromos_102": [51.15, 90.39, 43.09, 178.21, 211.79, 450.28]
    })

print(df_ventas)