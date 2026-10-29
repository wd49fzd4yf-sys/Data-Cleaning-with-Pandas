#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


# Question 1: Compute the euclidean distance between series (points) p and q, without using a packaged formula
input
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


# In[ ]:


dist = ((p - q) ** 2).sum() ** 0.5
print(dist)   


# In[ ]:


# Question 2: Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
input
df = pd.DataFrame(np.arange(20).reshape(-1,5), columns=list('abcde'))


# In[ ]:


df = df[['c', 'b', 'a', 'd', 'e']]
print(df)


# In[ ]:


# Question 3: Change the order of columns of a dataframe. Create a generic function to interchange two columns, without hardcoding column names.
def swap_columns(df, col1, col2):
    cols = list(df.columns)
    i, j = cols.index(col1), cols.index(col2) #find their positions
    cols[i], cols[j] = cols[j], cols[i] #swap the names in the list
    return df[cols]                 #reorder the dataframe

df = swap_columns(df, 'a', 'c')
print(df)


# In[ ]:


# Question 4: Format of suppress scientific notations in a pandas dataframe. Suppress scientific notations like 'e-03'
# in df and print upto 4 numbers after decimal. 
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])


# In[ ]:


pd.set_option('display.float_format', '{:.4f}'.format)
print(df)


# In[ ]:


# Question 5 Create a new column that contains the row number of nearest column by euclidean distance. Create a new column such that
# each row contains the row number of nearest row-record by euclidean distance.
input
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), 
columns=list('pqrs'), index=list('abcdefghij'))


# In[ ]:


nearest_rows = []
nearest_dists = []

for i, row in df.iterrows():
    dists = {}
    for j, other in df.iterrows():
        if i != j:                        #skip comparing a row to itself
            d = ((row - other) ** 2).sum() ** 0.5
            dists[j] = round(d)
    best = max(dists, key=dists.get)
    nearest_rows.append(best)
    nearest_dists.append(float(dists[best]))

df['nearest_row'] = nearest_rows
df['dist'] = nearest_dists
print(df)


# In[ ]:


# Question 6 Correlation is a statistical technique that shows how two variable are related. Correlation matrix
data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]}


# In[ ]:


df = pd.DataFrame(data)
print(df.corr())


# In[ ]:




