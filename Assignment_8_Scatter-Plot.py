#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 8 (3/3) - Scatter Plot
# October 28, 2019

import pandas as pd                     # Import pandas library
import numpy as np                      # Import numpy library
import matplotlib.pyplot as plt         # Import matplotlib.pyplot as plot; show plot in same window (inline)
get_ipython().run_line_magic('matplotlib', 'inline')

Location = "Datasets/gradedata.csv"     # Location of data csv file
df = pd.read_csv(Location)              # Create 'df' dataframe using data from csv file
df.head(3)                              # Show first three rows of the dataframe


# In[ ]:


plt.scatter(df['hours'], df['grade'])   # Create scatter plot using hours on the x-axis and grade on the y-axix

