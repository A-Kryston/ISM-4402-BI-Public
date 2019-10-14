#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Andrea Kryston
# Assignment #6 - Regression (pg 63)
# Due Date - October 14, 2019

import pandas as pd                   # Import pandas library
Location = "Datasets/gradedata.csv"   # Locate file to be used for this exercise
df = pd.read_csv(Location)            # Create 'df' dataframe from gradedata.csv file
df.head()                             # View first five rows to verify dataframe


# In[ ]:


def gender_to_number(x):   # Define a function to convert text 'gender' to a number representation of 'gender'
    if x == 'female':      # 'If' statement will convert the female values to 1
        return 1
    if x == 'male':        # 'If' statement will convert the male values to 0
        return 0


# In[ ]:


df['gender_val'] = df['gender'].apply(gender_to_number)   # Creates new 'gender_val' column that contains
                                                          # the numeric value of gender,
                                                          # as defined by the 'gender_to_number' function

df.tail()   # View the last five rows to verify dataframe


# In[ ]:


# Regression (Round 1 of 3)

import statsmodels.formula.api as sm   # Import statsmodels package

result = sm.ols(formula='grade ~ age + exercise + hours + gender_val', data=df).fit()   # Run regression model using variables
                                                                                        # shown in the formula,
                                                                                        # for data in 'df' dataframe
                                                                                        # and fit the model

result.summary()   # View results summary, paying particular attention to R-squared and p-values

# R-squared:  0.665
# p-values:  age (.587) stands out as not relevant, so 2nd regression round that excludes age variable will be done next


# In[ ]:


# Regression (Round 2 of 3)

import statsmodels.formula.api as sm   # Import statsmodels package

result = sm.ols(formula='grade ~ exercise + hours + gender_val', data=df).fit()   # Run 2nd round regression model
                                                                                  # where 'age' variable has been
                                                                                  # excluded from the formula

result.summary()   # View results summary, paying particular attention to R-squared and p-values

# R-squared:  0.665
# p-values:  gender_val (.077) is slightly above the .05 threshhold, so 3rd regression round  
#            that excludes gender_val variable will be done next


# In[ ]:


# Regression (Round 3 of 3)

import statsmodels.formula.api as sm   # Import statsmodels package

result = sm.ols(formula='grade ~ exercise + hours', data=df).fit()   # Run 3rd round regression model where the
                                                                     # 'gender_val' variable has been excluded

result.summary()   # View results summary, paying particular attention to R-squared and p-values

# R-squared:  0.665
# p-values:  At 0.000, both 'exercise' and 'hours' variables appear to be relevant in predicting 'grade'

# Using the coefficients from the results summary, the regression equation would be as follows:
# Grade = 58.5316 + 0.9892(exercise amount) + 1.9162(hours of study)

