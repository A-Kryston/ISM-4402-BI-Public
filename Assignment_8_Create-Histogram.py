#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 8 (1/3) - Create Histogram (pg 82)
# October 28, 2019

import matplotlib.pyplot as plt         # Import matplotlib.pyplot library
import pandas as pd                     # Import pandas library
                                        # Plot to be shown in same window (inline)
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "Datasets/gradedata.csv"     # Identifies location of gradedata file
df = pd.read_csv(Location)              # Create 'df' dataframe from data in gradedata csv file
df.head()                               # Shows first five rows of dataframe


# In[ ]:


df.hist(column="age",by="gender")       # Create histograms by gender, categorized by age

