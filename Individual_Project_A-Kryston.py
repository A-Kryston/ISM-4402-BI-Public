#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Analysis Exercise #2
# Due Date: December 2, 2019

import pandas as pd                    # Import various libraries
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import sys
import seaborn as sb
plt.style.use('seaborn')

Location = "Datasets/axisdata.csv"     # Identify location of file
df = pd.read_csv(Location)             # Create data frame from the file
df.head()                              # Display the first five rows of the data frame


# In[ ]:


df['Cars Sold'].mean()   # 1 - Avg cars sold per month


# In[ ]:


df['Cars Sold'].max()   # 2 - Max cars sold per month


# In[ ]:


df['Cars Sold'].min()   # 3 - Min cars sold per month


# In[ ]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])   # 4 - Avg cars sold per month by gender


# In[ ]:


df[df['Cars Sold']>3]['Hours Worked'].mean()   # 5 - Avg hours worked by people selling more than 3 cars per month


# In[ ]:


df['Years Experience'].mean()   # 6 - Avg years of experience


# In[ ]:


df[df['Cars Sold']>3]['Years Experience'].mean()   # 7 - Avg years of experience for people selling more than 3 cars per month


# In[ ]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])   # 8 - Avg cars sold per month sorted by sales training


# In[ ]:


df['Gender'].describe()   # Statistics about the Gender column indicate the split of men and women in the data is about 50/50


# In[ ]:


df['SalesTraining'].describe() # Statistics about the SalesTraining column indicate that about 58.6% of people received training


# In[ ]:


# Visualization 1 - Shows the distribution of Cars Sold, using side-by-side graphs for comparison,
#                   based on whether the employee was Not Trained (N) or Trained (Y).

axhist = df.hist(column="Cars Sold", by="SalesTraining",bins=7,sharex=True,sharey=True,edgecolor="Black",alpha=.90)
for ax in axhist.flatten():
    ax.set_xlabel("Cars Sold")
    ax.set_ylabel("Count")


# In[ ]:


# Visualization 2 - Utilizes box plots to compare basic statistics about Cars Sold based on Sales Training status.
#                   This representation provides Min, 1st Quartile, Median, 3rd Quartile, and Max data points.

sb.boxplot( x=df["SalesTraining"], y=df["Cars Sold"], palette="Blues")


# In[ ]:



# Miscellaneous visualizations follow.  These are some of my attempts to learn about what I could do with Python.
# For the purposes of this assignment, the write-up and presentation are based on Visualizations 1 and 2 above.


# In[ ]:


# Histograms for Cars Sold, by Years of Experience.  These graphs are not surprising (nor are they very interesting
# in my opinion) and generally confirm that those with only 1 year of experience are being outperformed 
# by those with more experience.

axhist = df.hist(column="Cars Sold", by="Years Experience",bins=7,sharex=True,sharey=True,edgecolor="Black",alpha=.8)
for ax in axhist.flatten():
    ax.set_xlabel("Cars Sold")
    ax.set_ylabel("Count")


# In[ ]:


# Bar plot shows average years of experience by gender; 
# there is not a significant difference between the averages for each gender.

sys.__stdout__ = sys.stdout
sb.barplot(x='Gender', y='Years Experience', data=df)
plt.show()


# In[ ]:


# Bar plot shows average number of cars sold by employees, compared by sales training status.  
# This comparison shows that employees who receive training have a higher average of "cars sold"
# than the untrained group.

sys.__stdout__ = sys.stdout
sb.barplot(x='SalesTraining', y='Cars Sold', data=df)
plt.show()

