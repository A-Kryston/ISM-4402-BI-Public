#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 2 (Load Multiple Excel Files)
# Due Date: 09-16-2019

import pandas as pd
import numpy as np
import glob

all_data = pd.DataFrame()  # Creates new blank dataframe
for f in glob.glob("Datasets/Weekly_Data_Files/weekdata*.xlsx"):   # Loops through the Excel files in the specified directory
    print (f)              # Informational only - confirms that all files were located
    df = pd.read_excel(f)  # Reads the Excel files
    all_data = all_data.append(df,ignore_index=True)   # Appends the contents of the Excel files into the new dataframe
all_data.describe()           # Informational only - confirms count and other statistics


# In[ ]:


all_data.head()     # Displays first five rows of data
                    # Instructor Daniel,
                    # Eventhough I used "ignore_index" as the author did,
                    # I am still seeing the first "index" column displayed in the data.
                    # I did research this, but was not able to determine how to fix it yet.
                    # I'm not sure how critical this is for the assignment, 
                    # so I am submitting the code as is for now.  ak


# In[ ]:




