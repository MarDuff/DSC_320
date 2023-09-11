#!/usr/bin/env python
# coding: utf-8

# ## Scatterplots and Linear Regression

# In[1]:


#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


#import data
data= pd.read_csv("car_data.csv")


# In[3]:


#preview the data
data.head()


# ## step 1

# In[14]:


#scatterplot
data = data
plt.xlabel("weight")
plt.ylabel("miles per gallon")
plt.plot(data['weight'],data['hwy_mpg'],".")
plt.show()


# In[15]:


#Based on the plot, the general trend of how highway miles 
per gallon varies with the weight is a decreasing function.


# In[ ]:


#If I was to build a linear model using this data to predict highway miles per gallon from 
weight, I would expect the slope to be negative because the mile per gallon is 
decreasing while the weight increase.


# ## step 4

# In[ ]:


#interpreting slope
the slope being −0.05 means that its a decreasing linear function.


# ## step 5

# In[94]:


#Write code to add a line to the graph you made in problem (1)


# In[96]:


reg= np.polyfit(data['weight'],data['hwy_mpg'], deg=1)
reg


# In[97]:


trend=np.polyval(reg,data['weight'])
plt.xlabel("weight")
plt.ylabel("miles per gallon")
plt.plot(data['weight'],data['hwy_mpg'],".")
plt.plot(data['weight'],trend);


# In[98]:


#the slope is -1.05471572e-02 and the y-intercept is 5.77051742e+01


# ## Point 6

# In[99]:


#find the best-fit line
best_slope = theta_all[-1]
best_slope


# In[16]:


#create the variables X and y from the Pandas dataframe
X = data['weight'].to_numpy().reshape(-1, 1)
X.shape


# In[17]:


y = data['hwy_mpg'].to_numpy().reshape(-1, 1)
y.shape


# In[107]:


from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model


# In[29]:


standard_scaler = StandardScaler()
X = standard_scaler.fit_transform(X)
y = standard_scaler.fit_transform(y)


# In[53]:


x=data['weight'].tolist()
y=data['hwy_mpg'].tolist()


# In[108]:


metrics.mean_square_error(x,y)


# In[63]:


regr = linear_model.LinearRegression()


# In[62]:


regr.fit(x, y)


# In[59]:


theta=0
m=205
def MSE_derivative(x, y, theta=0): m = y.shape[0]
cost_derivative = (1 / 205) * np.sum((0 * x - y) * x) 
return cost_derivative


# In[30]:


MSE_derivative(x=X, y=y, theta=0)


# In[ ]:




