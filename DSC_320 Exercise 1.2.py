#!/usr/bin/env python
# coding: utf-8

# ## Mathematical and Python Functions
# 

# In[5]:


#import libraries
import numpy as np #library for arrays and matrices
import pandas as pd # library for data frames
import matplotlib.pyplot as plt #library for for data vizualisation


# In[7]:


#import data with pandas
data= pd.read_csv("housing_data.csv")
#display the first rows of dataset
data.head()


# In[47]:


#create numpy arrays 
actual_values = np.array(['sale_price'])
predicted_values = np.array(['sale_price_pred'])


# In[50]:


#get a summary of data
data.describe()


# In[8]:


#get the shape of data
data.sort_values('sale_price')


# In[9]:


#get arrays from the dataset
actual_values = data['sale_price'].tolist()
predicted_values= data['sale_price_pred'].tolist()

array1= np.array([actual_values])
array2= np.array([predicted_values])


# ## create mathematical functions to find RMSE
# 

# In[72]:


#get the difference of the arrays
diff=array2 - array1
diff


# In[71]:


#get the square of arrays difference
sq_diff=np.square(array2-array1)
sq_diff


# In[74]:


#get the sum of the square differences
sq_diff_sum= np.sum(sq_diff)
sq_diff_sum


# In[76]:


#get count of numerical data
n=data.count()
n


# In[85]:


#get the square root of sum of values
Num= np.sqrt(sq_diff_sum)


# In[104]:


#get the square root of n
Denom= np.sqrt(n)
Denom


# In[3]:


#create the RMSE function RMSE= squareroot (1/n[(yb1 −y1) +(yb2 −y2) +...+(ybn −yn) ]).

def Root_mean_squared_error():
    np.divide(Num, Denom)

print(Root_mean_squared_error)


# ## create mathematical functions to find MAE

# In[17]:


#create arrays from dataset
actual_values = data['sale_price'].tolist()
predicted_values= data['sale_price_pred'].tolist()

array1= np.array([actual_values])
array2= np.array([predicted_values])


# In[18]:


#get the difference of arrays
diff= array2 - array1
diff


# In[23]:


#get the count of the sample
n= data.count
print(n)


# In[25]:


#get the Mean Absolute Error (MAE)
def mean_absolute_error():
    np.multiple(diff,1/1460)
    
print(mean_absolute_error)


# ## point 3

# In[30]:


#create arrays from dataset
actual_values = data['sale_price'].tolist()
predicted_values= data['sale_price_pred'].tolist()

array1= np.array([actual_values])
array2= np.array([predicted_values])
print(array1)
print(array2)


# In[32]:


#a getting accuracy
len(array1)==len(array2)


# In[33]:


data2= pd.read_csv('mushroom_data.csv')


# In[34]:


#get the summary of the data
data2.describe()


# In[39]:


#getting the arrays to compare
actual_values = data2['actual'].tolist()
predicted_values= data2['predicted'].tolist()

array3= np.array(['actual'])
array4= np.array(['predicted'])


# In[40]:


len(array3)==len(array4)


# ## point 4

# In[65]:


x_values=array4


# In[66]:


def f(p): return (x_values,0.005*p^6-0.27*p^5+5.998*p^4-69.919*p^3+449.17*p^2-1499.7*p=2028

