#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment #6 - Sort columns in a dataframe (pg 60)
# Due Date - October 14, 2019

import pandas as pd                   # Import pandas library
Location = "Datasets/gradedata.csv"   # Locate file to be used for this exercise
df = pd.read_csv(Location)            # Create df dataframe from gradedata.csv file
df.head()                             # View first five rows to verify dataframe


# In[ ]:


df = df.sort_values(by=['lname','age','grade'], ascending=[True,True,False])  # Sort the dataframe as follows: 
                                                                              # 'lname' column (ascending order) 
                                                                              # 'age' column (ascending order)
                                                                              # 'grade' column (descending order)
df.head()   # View first five rows to verify dataframe

