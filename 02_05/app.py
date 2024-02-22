import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_edad =  pd.DataFrame({
    'grupo_1': np.random.normal(18, 45, 1000),
    'grupo_2': np.random.normal(18, 45, 1000)
})