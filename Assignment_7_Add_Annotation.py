#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 7 - Add Annotation (Page 74)
# Due Date:  October 21, 2019

import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades'])

get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[ ]:


import matplotlib.pyplot as plt

df.plot()
displayText = "Wow!"
xloc = 0
yloc = 76
xtext = 180
ytext = 100
plt.annotate(displayText, 
            xy=(xloc, yloc), 
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')


# In[ ]:


df.plot()
displayText = "Wow!"
xloc = 0
yloc = 76
xtext = 180
ytext = 100     
plt.annotate(displayText, 
            xy=(xloc, yloc), 
            arrowprops=dict(facecolor='black', shrink=0.05),   
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')

