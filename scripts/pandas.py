
# coding: utf-8

# ## Getting and Inspecting Data

# In[ ]:

import numpy as np
import pandas as pd

df = pd.read_csv('../data/drive.csv')
df.head()


# In[ ]:

print(df.shape, df.columns, df.dtypes)
df['Game Code'][10:25]
df.describe()


# ## Cleaning data

# In[ ]:

df.isna().sum()


# In[ ]:

df = df.dropna()


# ## Challenge: Counting Values

# In[ ]:

N = df['End Reason'].count()
df['End Reason'].value_counts()*100./N


# ## Challenge: Describing Only *Some* Data

# In[ ]:

td = df[df['End Reason']=='TOUCHDOWN']
td['Time Of Possession'].describe()


# ## Challenge: The Best Team?

# In[ ]:

df['Yards Per Play'] = df['Yards']/df['Plays']
teams_grouped = df.groupby(['Team Code'])
teams_grouped_mean = teams_grouped['Yards Per Play'].mean()
teams_grouped_mean.sort_values(ascending=False).head()


# In[ ]:



