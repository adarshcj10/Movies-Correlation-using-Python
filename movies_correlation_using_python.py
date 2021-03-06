# -*- coding: utf-8 -*-
"""Movies Correlation Using Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18PJJHPUSRgz0fvhaHZLGsJ3L3Xk0Z-W0
"""

# Commented out IPython magic to ensure Python compatibility.
# Importing packages 
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

# %matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

df = pd.read_csv('/Users/adarshcj/Downloads/movies.csv')

df

# Let's see if we have any missing data
# Using loop function through the data to see if there is anything missing

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))

# Data Types for the columns

print(df.dtypes)

# Changing data type(data cleaning step)

df['budget'] = df['budget'].astype('float64')
df['gross'] = df['gross'].astype('float64')

df['yearcorrect'] = df['released'].astype(str).str[:4]

df.sort_values(by=['gross'], inplace=False, ascending=False)

pd.set_option('display.max_rows', None)

# Dropping duplicates

df['company'].drop_duplicates().sort_values(ascending=False)

df.drop_duplicates()

# Plotting Graphs

plt.scatter(x=df['budget'], y=df['gross'])
plt.show()

# Plot Budget vs gross using Seaborb
sns.regplot(x="budget", y="gross", data=df, scatter_kws={"color": "green"}, line_kws={"color": "blue"})

# Looking at the Correlations using Pearson method

df.corr(method='pearson')

# Plotting Correlation 

correlation_matrix = df.corr()

sns.heatmap(correlation_matrix, annot = True)

df_numerized = df


for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name]= df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
        
df_numerized

correlation_matrix = df_numerized.corr(method='pearson')

sns.heatmap(correlation_matrix, annot = True)

plt.title("Correlation matrix for Movies")

plt.xlabel("Movie features")

plt.ylabel("Movie features")

plt.show()

correlation_mat = df.apply(lambda x: x.factorize()[0]).corr()

corr_pairs = correlation_mat.unstack()

print(corr_pairs)

sorted_pairs = corr_pairs.sort_values(kind="quicksort")

print(sorted_pairs)

# We can now take a look at the ones that have a high correlation (> 0.5)

strong_pairs = sorted_pairs[abs(sorted_pairs) > 0.5]

print(strong_pairs)

