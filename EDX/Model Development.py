#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Elona Zharri
# 06/24/2020
# In this section I will develop several models that will predict the price
# of the car using the variables or features. This is just an esimate
# but should give us an objective idea of how much the car should cost.

# Model Development helps us predict future observations from the data we have.
# A model will help us understand the exact relationship btw different variables
# and how these variables are used to predict the result.

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

# Linear Regression and Multiple Linear Regression
# Simple Linear Regression is a method to help us understand the relationship btw 2 variables:
# 1.the predictor/independent variable (X)
# 2.the response/dependent variable (that we want to predict)(Y)
# The result of Linear Regression is a linear function that predicts the response (dependent)
# variable as a function of the predictor (independent) variable.
# Y: Response Variable
# X: Predictor Variables
# Linear function: Yhat = a+bX
# a refers to the intercept of the regression line0, in other words: the value of Y when X is 0
# b refers to the slope of the regression line, in other words: the value with which Y changes when X increases by 1 unit

#Lets load the modules for linear regression
from sklearn.linear_model import LinearRegression

# create the linear regression object
lm = LinearRegression()
lm

# how could Highway-mpg help us predict car price?
X = df[['highway-mpg']]
Y = df['price']

# fit the linear model using highway-mpg
lm.fit(X,Y)

# We can output a prediction
Yhat=lm.predict(X)
Yhat[0:5]

#What is the value of intercept(a)
lm.intercept_

#What is the value of the Slope(b)
lm.coef_

#what is the final estimated linear model we get?
# Yhat = a + bX

# Create a linear regression object
lm1= LinearRegression()
lm1

# Train the model using 'engine-size' as the independent variable 'price' as the dependent variable
lm1.fit(df[['engine-size']],[['price']])
lm1

# Find the slope and intercept of the model
lm.coef_
lm.intercept_

# Multiple Linear Regression
# If we want to use more variables in our model to predict car price, we can use Multiple Linear Regression.
# Multiple Linear Regression is very similar to Simple Linear Regression, but this method is used to explain 
# the relationship between one continuous response (dependent) variable and two or more predictor (independent) variables.

# Yhat = a + b_1 X_1 + b_2 X_2 + b_3 X_3 + b_4 X_4

Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]

# Fit the linear model using the four above mentioned variables
lm.fit(Z, df['price'])
lm.intercept_
lm.coef_

lm2 = LinearRegression()
lm2.fit(df[['normalized-losses', 'highway-mpg']], df['price'])

# Model Evaluation using Visualization
import seaborn as sns

# Regression Plot
# When it comes to simple linearregression, an excellent way to visualize the fit of our model is by using regression plots
# This plot will show a combination of a scattered data points (a scatter plot)
# as well as the fitted linear regressionline going through the data.
# This will give us a reasonable estimate of the relationship btw the two variables
# the strength of the correlation, as well as the direction (positive or negative correlation)

# Lets visualize Horsepower as potential predictor variable of price

width = 12
height = 10
plt.figure(figsize=(width,height))
sns.regplot(x="highway-mpg", y="price", data=df)
plt.ylim(0,)

plt.figure(figsize=(width, height))
sns.regplot(x="peak-rpm", y="price", data=df)
plt.ylim(0,)

df[["peak-rpm", "highway-mpg", "price"]].corr()

# Residual Plot
# A good way to visualize the variance of the data is to use a residual plot
# What is a residual?
# The difference btw the observed value (y) and the redicted value (Yhat) is called the residual (e).
# When we look at a regression plot, the residual is the distance from the data point to the fitted regression line
# A residual plot is a graph that shows the residuals on the vertical y-axis and the independent variable on the horizontal x-axis
# We pay attention to the spread of the residuals.
# if the points in a residual plot are randomly spread out around the x-axis
# then a linear model is appropriate for the data.
# Randomly spread out residuals means that the variance is constant, and thus the linear model is a good fit for this data

width = 12
height = 10
plt.figure(figsize=(width, height))
sns.residplot(df['highway-mpg'], df['price'])
plt.show()

# Multiple Linear Regression
Y_hat = lm.predict(Z)
plt.figure(figsize=(width,height))

ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplo(Yhat, hist=False, color="b", label="Fitted Values", ax=ax1)

plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price(in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()


# In[ ]:




