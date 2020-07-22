import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import seaborn as sns

df = pd.read_csv('data.csv')

print df

df2 = df.pivot_table(index='year',columns='continent', values='lifeExp')
print df2

sns.heatmap(df2).get_figure().savefig('heatmap.png')