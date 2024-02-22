import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_ventas = pd.DataFrame(
    {
        "cromos": ["Cromo 101", "Cromo 102"] * 6,
        "ventas": [100, 150, 200, 123,258, 156,369, 212,567, 234,123, 890],
    }
)