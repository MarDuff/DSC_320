#!/usr/bin/env python
# coding: utf-8

# ## US Population Growth

# In[1]:


#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# ## Question 1

# In[5]:


#mport the data and create two new columns.
df= pd.read_csv('us_pop_data.csv')
df.head()


# ### Point a)

# In[7]:


#Create one column that is the number of years since 1790
#Create another column that is the population in millions.
df['n_years'] = df['year'] - 1790
df['pop_m'] = df['us_pop'] / 1e7
df.head()


# ### Point b)

# In[9]:


#Plot the US population (in millions) versus the years since 1790
data=df
plt.xlabel("year since 1790")
plt.ylabel("Population(Millions)")
plt.plot(df['n_years'],df['pop_m'],".")
plt.show()


# ### Point c)

# In[10]:


#Create a linear regression model to predict the US population (in millions) t years from 1790.
#Find and report the R2-value of this model.
#We want to predict population by using years
# population - y
# years - x
y = df['pop_m'].to_numpy()
X = df['n_years'].to_numpy()
print("Before reshape", X.shape)


# In[11]:


X = X.reshape(-1, 1)
y = y.reshape(-1, 1)
print("After reshape", X.shape)


# In[12]:


# model fitting
model = LinearRegression(fit_intercept=True)
model.fit(X, y)


# In[13]:


# y = mx + b
print("Intercept (b): ", model.intercept_)
print("Slope (m):     ", model.coef_)
print("R^2:           ", model.score(X, y))


# ### Point d)

# In[15]:


#Create another new column in your data by squaring the number of years since 1790
df['n_years_sq'] = df['n_years']**2
df.head()


# ### Point e)

# In[16]:


y = df['pop_m'].to_numpy().reshape(-1, 1)
X = df['n_years_sq'].to_numpy().reshape(-1, 1)

model2 = LinearRegression(fit_intercept=True)
model2.fit(X, y)

print("Intercept (b): ", model2.intercept_)
print("Slope (m):     ", model2.coef_)
print("R^2:           ", model2.score(X, y))


# ### Point f)

# In[20]:


plt.xlabel('years')
plt.ylabel('Population(Millions)')
plt.plot(df['n_years'], df['pop_m'])
# arg1 - intercept as a coordinate (0, intercept)
# arg2 - slope 
# Have to use indexing because (as seen above) the intercept is provided as a list
# and the slope is provided as a list inside a list
plt.axline((0, model.intercept_[0]), slope=model.coef_[0][0],color='r')


# In[22]:


plt.xlabel('years')
plt.ylabel('Population(Millions)')
plt.plot(df['n_years_sq'], df['pop_m'])
# arg1 - intercept as a coordinate (0, intercept)
# arg2 - slope 
plt.axline((0, model2.intercept_[0]), slope=model2.coef_[0][0], color= 'r')


# ## Question 2

# In[29]:


#import data
data= pd.read_csv('customer_spending.csv')
data.head()


# ### Point a)

# In[25]:


#Make a histogram of the customer spending amounts.
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


# In[14]:


plt.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color='Blue' , *, data=None, **kwargs)


# ### Point b)

# In[ ]:


#Make a new data set that is a log transformation of the customer spending amounts.

