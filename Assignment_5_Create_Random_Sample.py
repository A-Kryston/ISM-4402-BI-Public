#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 5 - Create Random Sample from Dataset (pg. 53)
# Due Date - October 7, 2019

import pandas as pd                  # Import pandas library
import numpy as np                   # Import numpy library
Location = "Datasets/gradedata.csv"  # Locate file to be used for this exercise
df = pd.read_csv(Location)           # Create 'df' dataframe from the gradedata.csv file
df.head()                            # View first five rows to verify dataframe


# In[ ]:


df.take(np.random.permutation(len(df))[:500])    # Randomly takes a sample of 500 rows from the 'df' dataframe

