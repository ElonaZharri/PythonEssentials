#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Elona Zharri
# 06/23/2020

import pandas as pd
import numpy as np

path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
#df.head()

# to install seaborn we use pip which is a python package manager
# %%capture
# ! pip install seaborn

# now will import visualization packages "Matplotlib" and "Seaborn"
import matplotlib.pyplot as plt
import seaborn as sns

#print(df.dtypes)
# to find the correlation
df.corr()

# finding the correlation between the specified columns
df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()

# Continuous numerical variables are variables that may contain any value
# within some range. A great way to visualize these variables is by using
# scatterplots with fitted lines.

# Positive linear relationship
# Let's find the scatterplot of "engine-size" and "price"
# Engine size as potential predictor variable of price
sns. regplot(x="engine-size", y="price", data= df)
plt.ylim(0,)

# we can examine the correlation btw "highway-mpg" and "price"
df[["highway-mpg", "price"]].corr()
sns.regplot(x="peak-rpm", y="price", data=df)

# Weak Linear Relationship
# Let's see if "Peak-rpm" as a predictor variable of "price"
sns.regplot(x="peak-rpm", y="price", data=df)

# Peak rpm does not seem like a good predictor of the price at all since 
# the regression line is close to horizontal. Also, the data points are very
# scattered and far from the fitted line, showing lots of variability.
# Therefore it's not a reliable variable.
df[['peak-rpm','price']].corr()

# Categorical Variables
# These are variables that decribe a "characteristic" of a data unit & are selected
# from a small group of categories. The categorical variables can have the type
# "object" or "int64". A good way to visualize categorical variables is using boxplots.
sns.boxplot(x="body-style", y="price", data=df)
sns.boxplot(x="engine-location", y="price", data=df)

# Descriptive Statistical Analysis
# The describe function automatically computes basic statictics for all continuous variables
# The default setting of "describe" skips variables of type "object".
df.describe(include=["object"])

# Value Counts
# Value-counts is a good way of understanding how many units of each
# characteristic/variable we have. Value_counts only works on pandas series, not Pandas Dataframes
# As a result, we only include one bracket "df['drive-wheels']" not two brackets "df[['drive-wheels']]".

df['drive-wheels'].value_counts()

# We can convert the series to a Dataframe as follows
df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
drive_wheels_counts

# Now let's rename the index to 'drive-wheels':
drive_wheels_counts.index.name = 'drive-wheels'
drive_wheels_counts

# Basic Grouping
# The "groupby" method groups data by different categories. The data is grouped
# based on one or several variables and analysis is performed on the individual groups

df['drive-wheels'].unique()

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#Let's use a heat map to visualize the relationship between Body Style vs Price.
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()


# In[2]:


# Correlation and Causation
# Correlation:a measure of the extent of interdependence btw variables
# Causation: the relationship btw causes and effect btw 2 variables
# It is important to know the difference btw these two and that correlation does not imply causation.
# Determining correlation is much simpler than determining causation as causation may require independent experimentation

# Pearson Correlation
# It measires the linear dependence btw 2 variables X and Y
# Pearson correlation is the default method of the function "corr"
# We can calculate the Pearson Correlation of the 'int64' or 'float64' variables

df.corr()

# P-Value


# In[ ]:




