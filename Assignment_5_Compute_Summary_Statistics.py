#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 5 - Compute Summary Statistics (pg. 57)
# Due Date - October 7, 2019

import pandas as pd                             # Import pandas library

names = ['Bob','Jessica','Mary','John','Mel']   # Create list of names to be used in dataframe
grades = [76,95,77,78,99]                       # Create list of grades to be used in dataframe
bsdegrees = [1,1,0,0,1]                         # Create list of bs degree data to be used in dataframe
msdegrees = [2,1,0,0,0]                         # Create list of ms degree data to be used in dataframe
phddegrees = [0,1,0,0,0]                        # Create list of phd degree data to be used in dataframe

GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)   # Combine (zip) lists to create GradeList 
df = pd.DataFrame(data = GradeList, columns=['Names','Grades','BS','MS','PhD'])   # Create 'df' dataframe using GradeList data
                                                                                  # and add column names/labels
df   # View 'df' dataframe


# In[ ]:


# Generate summary statistics for the dataset


# In[ ]:


df.count()  # Computes the count of the values


# In[ ]:


df.mean()   # Computes the mean (arithmetic average) of the values


# In[ ]:


df.std()    # Computes the standard deviation of the values


# In[ ]:


df.min()    # Computes the minimum of the values


# In[ ]:


df.max()    # Computes the maximum of the values


# In[ ]:


df.quantile(.25)    # Computes the highest value in the lowest 25% of the data (first-quartile)


# In[ ]:


df.quantile(.50)    # Computes the highest value in the lowest 50% of the data (second-quartile)


# In[ ]:


df.quantile(.75)    # Computes the highest value in the lowest 75% of the data (third-quartile)

