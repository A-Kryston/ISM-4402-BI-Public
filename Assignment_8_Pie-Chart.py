#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 8 (2/3) - Pie Chart
# October 28, 2019

import pandas as pd                                      # Import pandas library
import matplotlib.pyplot as plt                          # Import matplotlib.pyplot library; create plot on same sheet (inline)
get_ipython().run_line_magic('matplotlib', 'inline')

names = ['Bob','Jessica','Mary','John','Mel']            # Manual creation of data for dataframe ()
absences = [3,0,1,0,8]
detentions = [2,1,0,0,1]
warnings = [2,1,5,1,2]

GradeList = zip(names,absences,detentions,warnings)      # Combine the data above into GradeList object
columns=['Names', 'Absences', 'Detentions', 'Warnings']  # Create column names
df = pd.DataFrame(data = GradeList, columns=columns)     # Create 'df' dataframe

df                                                       # Show 'df' dataframe


# In[ ]:


df['TotalDemerits'] = df['Absences'] + df['Detentions'] + df['Warnings']   # Create new column called 'Total Demerits' 
                                                                           # which provides sum of all types of demerits
df                                                                         # Show 'df' dataframe


# In[ ]:


plt.pie(df['TotalDemerits'])          # Plot pie chart for 'TotalDemerits' data


# In[ ]:


plt.pie(df['TotalDemerits'],          # Adjust pie chart to be more understandable and useful by
       labels=df['Names'],            # adding lables,
       explode=(0,0,0,0.25,0),        # highlighting individual with fewest demerits, and
       startangle=150,                # rotating the pie chart
       autopct='%1.1f%%',)

plt.axis('equal')                     # Make x-axis and y-axis equal
plt.show()                            # Show pie chart

