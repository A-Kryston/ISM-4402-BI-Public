#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 7 - Status as Label (pg 76)
# Due Date:  October 21, 2019

import matplotlib.pyplot as plt
import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(names,status,grades)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Status', 'Grades'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')


# In[ ]:


df2 = df.set_index(df['Status'])
df2.plot(kind="bar")

