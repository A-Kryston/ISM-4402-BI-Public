#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 4 - Add Pass/Fail Column Using Bins
# September 30, 2019

import pandas as pd                   # Import pandas library
Location = "Datasets/gradedata.csv"   # Locate the file to be used for this exercise
df = pd.read_csv(Location)            # Create 'df' dataframe from gradedata.csv file
df.head(2)                            # View to verify dataframe


# In[ ]:


bins = [0,80,100]                     # Create bins to segment scores to flag as pass/fail
status_names = ['Fail','Pass']        # Create pass/fail lables to be used in new column
df['status'] = pd.cut(df['grade'],bins,labels=status_names) # Add 'status' column indicating pass/fail based on bin parameters
df.head(2)                            # View to verify dataframe with new 'status' column


# In[ ]:


pd.value_counts(df['status'])         # Provides counts of Pass/Fail statuses

