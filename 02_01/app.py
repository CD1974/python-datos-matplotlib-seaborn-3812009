import matplotlib.pyplot as plt
import pandas as pd

df_ventas = pd.DataFrame({
    'cromos': ['Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102', 'Cromo 101', 'Cromo 102'],
    'trimestre': ['T1', 'T1',  'T2', 'T2',  'T3', 'T3', 'T4', 'T4'],
    'ventas': [100, 150, 200, 123, 258, 156, 369, 212]
  })
