#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment 2 - Load data from a database
# Due Date: 09-16-2019

import pandas as pd
from sqlalchemy import create_engine

db_file = r'Datasets/salesdata.db'                            # Access the database file from specified directory
engine = create_engine(r"sqlite:///{}".format(db_file))       # Engine helps perform operations for the db file

sql = "select name from sqlite_master where type = 'table';"  # Determines which tables are available in the database

sales_data_df = pd.read_sql(sql, engine)                      # Stores the contents in sales_data_df dataframe
sales_data_df.head()                                          # Displays all available table names


# In[ ]:


sql = "select * from scores;"                                 # Selects all data from the 'scores' table
scores_df = pd.read_sql(sql, engine)                          # Stores the contents in scores_df dataframe
scores_df.head()                                              # Informational - displays all columns for first five rows


# In[ ]:




