#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Elona Zharri
# 06/21/2020
# Data Wrangling is the process of converting data from the initial format to a format 
# that may be better for analysis.

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# will first import the data
mydataset = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

# reading the dataset
df = pd.read_csv(mydataset, names=headers)
# use the method head() to display the first five rows of the dataframe.
df.head(5)

# working with missing values:
# 1.identify the missing data
# 2.deal with the missing data
# 3.correct data format

# we will replace "?" with NaN for reasons of computational speed and convenience
df.replace("?", np.nan, inplace = True)
df.head(5)

# evaluating for missing values
# 1. .isnull()
# 2. .notnull()
# the output is a boolean value: True stands for missing value, False stands for not missing value
missing_data = df.isnull()
missing_data.head(5)

# counting missing values in each column
# by using a for loop, we can quickly figure out the number of missing values

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
    
# now that we have identified our missing data, it's time to deal with it
# there couple options how to deal with missing data
# 1. drop data: drop the whole row or column
# 2. replace data: by mean, by frequency or based on other functions

# we will calculate the avg of the column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)
# we will now replace "NaN" by mean value in "normalized-losses" column
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace= True)

avg_stroke = df["stroke"].astype("float").mean(axis=0)
print("Average of stroke:", avg_stroke)
df["stroke"].replace(np.nan, avg_stroke, inplace = True)

avg_horsepower = df["horsepower"].astype("float").mean(axis = 0)
print("Average of stroke:", avg_horsepower)
df["horsepower"].replace(np.nan, avg_horsepower, inplace=True)


avg_peakrpm = df["peak-rpm"].astype("float").mean(axis=0)
print("Average of stroke:", avg_peakrpm)
df["peak-rpm"].replace(np.nan, avg_peakrpm, inplace=True)

# to see which values are present in a particular column
df['num-of-doors'].value_counts()

# we use ".idxmax()" to calculate the most common type automatically
df['num-of-doors'].value_counts().idxmax()

# replace the missing 'num-of-doors' values by the most frequent 
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# drop all rows that do not have price data
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we dropped two rows
df.reset_index(drop=True, inplace=True)


# In[18]:


# Normalization is the process of transforming values of several variables
# into a similar range.Typical normalization include scaling the variable so the variable avg is 0
# scaling the variable so the variance is 1, or scaling variable so the variable values range from 0 to 1

# we will replace the original value by original value/maximum value
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()

# showing the scaled columns
df[["length", "width", "height"]].head()


# In[20]:


# Binning is a process of transforming continuous numerical variables 
# into discrete categorical "bins", for grouped analysis.

# convert data to correct format
df["horsepower"]=df["horsepower"].astype(int, copy=True)

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot
plt.pyplot.hist(df["horsepower"])

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")


# In[21]:


# We build a bin array, with a minimum value to a maximum value, with bandwidth calculated above. 
# The bins will be values used to determine when one bin ends and another begins.
bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
bins


# In[22]:


# We set group names:
group_names = ['Low', 'Medium', 'High']


# In[23]:


# We apply the function "cut" the determine what each value 
# of "df['horsepower']" belongs to.
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
df[['horsepower','horsepower-binned']].head(20)

# Lets see the number of vehicles in each bin.
df["horsepower-binned"].value_counts()

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
from matplotlib import pyplot
pyplot.bar(group_names, df["horsepower-binned"].value_counts())

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

a = (0,1,2)

# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"], bins = 3)


# In[ ]:




