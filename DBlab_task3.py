#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


dataset = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Desktop\energy_train_1d_dirty.csv' , ';')


# In[5]:


#Cleaning_df_energy
dataset.drop_duplicates()

#Dropping Null values
dataset.dropna()

#Eleminating negative values
dataset = dataset[(dataset['value_max'] >= 0) & (dataset['value_avg'] >=0) & (dataset['value_min'] >=0)]
dataset.info()


# In[ ]:




