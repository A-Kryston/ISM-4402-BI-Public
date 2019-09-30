#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 4 - Add TimeMgmt Column (Using Conditionals)
# September 30, 2019

import pandas as pd                    # Import pandas library
Location = "Datasets/gradedata.csv"    # Locate file to be used for this exercise
df = pd.read_csv(Location)             # Create 'df' dataframe from gradedata.csv file
df.head()                              # View first five rows to verify dataframe


# In[ ]:


import numpy as np   # Import numpy library
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours']>17), 'busy' , 'normal') # Add 'timemgmt' column;
                                                                                    # conditionals used to populate new column
                                                                                    # with 'busy' or 'normal'
df.tail(10)          # View last 10 rows to verify dataframe with new column


# In[ ]:


pd.value_counts(df['timemgmt'])   # Provides counts of 'busy' and 'normal' statuses

