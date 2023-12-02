#!/usr/bin/env python
# coding: utf-8

# ### 1. Solving a System of Linear Equations
# 

# ##### Use Python to solve the following system of equations. Hint: You can write this system as a matrix equation in in the form Ax = b, where the matrix A is invertible.

# In[11]:


#import libraries
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


# In[12]:


A= np.array([[27, -10, 4, -29],
             [-16, 5, -2, 18],
             [-17, 4, -2, -20],
             [-7, 2, -3, 8]])

B=np.array([1, -1, 0, 1])


# In[15]:


print ("Solution:\n", np.linalg.
       solve(A, B ) )


# ### 2. Visualizing a Linear Transformation

# In[35]:


#(a) Find T(x), where x = [2,-2]
s2 = math.sqrt(2) / 2

T = np.array([[s2, -s2],
  [s2, s2]])
x=np.arange(2,-2)
y=np.arange(2,-2)


xx, yy = np.meshgrid(x, y)
trans = T@v
trans


# In[40]:


#(b) Mimic the code in Section 7.1.3 of Essential Math for Data Science to visualize the linear trans-
#formation T
T = np.array([[s2, -s2],
  [s2, s2]])

xy =  np.vstack([xx.flatten(), yy.flatten()])
xy.shape

xx_transformed = trans[0].reshape(xx.shape)
yy_transformed = trans[1].reshape(yy.shape)

f, axes = plt.subplots(1, 2, figsize=(6, 3)) 
axes[0].scatter(x, y, s=10, c=xx+yy) 
axes[1].scatter(xx_transformed, yy_transformed, s=10, c=xx+yy) 

# [...] Add axis, x and y witht the same scale


# In[ ]:




