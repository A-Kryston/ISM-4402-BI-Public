#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 3 (Replace Data)
# Due Date: 09-23-2019

# Create data to be used in this assignment

import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']                    # Create list of 'names' for dataset
grades = [76,-2,77,78,101]                                       # Create list of 'grades' for dataset

GradeList = zip(names,grades)                                    # Combine data 
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])  # Assign data to dataframe called df

df                                                               # View dataframe to confirm accuracy


# In[ ]:


# Assignment requirement is to replace all the subzero grades with a grade of zero

df.loc[(df['Grades'] <0, 'Grades')] = 0                        # Set grades less than zero to be zero; the book uses 'less
                                                               # than or equal to zero', but it seems unnecessary to change
                                                               # an existing zero to zero, so I used less than, only.

df                                                             # View dataframe to confirm accuracy (see Jessica's grade of 0)

