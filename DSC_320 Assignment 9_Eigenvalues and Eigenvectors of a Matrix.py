#!/usr/bin/env python
# coding: utf-8

# ### 1. Finding the Eigenvalues and Eigenvectors of a Matrix

# In[60]:


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


A= np.array([[4,0,1], 
            [-1, -6, -2],
           [5,0,0]])
A


# In[6]:


#Is the vector u=[1,2,3] an eigenvector of A? Verify your answer with a calculation in Python.

u=np.array([1,2,3])

A@u


# In[8]:


#Is the vector v=[0,1,0] an eigenvector of A? Verify your answer with a calculation in Python.
v=np.array([0,1,0])
A@v   
    


# ##### Answer: u is not a eigen value of A, However, v is an eigenvector of A because it is a scalar multiple of v.

# In[10]:


#(c) Use Python to find all of the eigenvalues and eigenvectors of A.
from numpy.linalg import eig

w,v=eig(A)
print('E-value:', w)
print('E-vector', v)



# ### 2. Principal Component Analysis

# In[13]:


#import data
data=pd.read_csv('video_game_data.csv')
data.head()


# In[43]:


#(a) Make a scatterplot of the user scores versus critics scores.

plt.scatter(data['user_score'],data['critic_score'])
plt.xlabel("user_score")
plt.ylabel("critic_score")


# In[48]:


#(b) On your scatterplot from part (a), 
#sketch the approximate directions of the first and second principal components. 

data.shape

