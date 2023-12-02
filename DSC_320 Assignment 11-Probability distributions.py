#!/usr/bin/env python
# coding: utf-8

# ### 1. Using the Binomial Distribution

# ##### An ensemble model is a model that uses multiple different models to build a better model. E.g., a random forest classifier uses multiple decision trees to “vote” for the best answer. For this exercise, assume that an ensemble model uses majority vote to predict a binary target and that each individual model is independent of every other model. Use Python code to answer the following questions.

# In[5]:


import math
import numpy as np
from scipy.stats import binom


# In[18]:


# (a) If an ensemble model is composed of 15 individual models that each have 63% accuracy, 
#what is the ensemble model accuracy?


np.sum([binom.pmf(k,15,0.63) for k in range(1,15)])


# In[25]:


# (b) What would the accuracy of the 15 individual models need to be in order for the ensemble
#model to have 95% accuracy? Find the smallest whole number percentage so this is satisfied.

np.sum([binom.pmf(k,15,0.95) for k in range(1,15)])


# In[232]:


# (c) If each individual model has 63% accuracy, 
#how many individual models are needed for the ensemble model to have 95% accuracy? 
#Find the smallest odd number of models (so there is a clear majority), 
#so that this is satisfied.

for k in range(1,15):
    ([binom.rvs(n=15,p=0.95,k)])


# ### 2. Working with Random Data

# #### Suppose that a random variable X can take on values 1, 2, 3, 4, or 5.

# In[131]:


# (a) Make up your own probability mass function (pmf) for X. 
#Make sure it satisfies the requirements of a pmf.
from scipy.stats import binom
X = np.random.choice(['1', '2', '3', '4', '5'])
X=binom.pmf(2, 5, 0.2)
print (X)


# In[228]:


#(b) Build a function that will generate 50 random X-values from the pmf you created 
#in part (a) and return the mean of these values.
import random 

def random_x():
    x = random.randint(1,5)
    return x 

def mean_x():
    sum = 0 
    for i in range(0,50):
        sum += generate_random_x() 
    mean = sum/50
    return mean 


# In[231]:


#(c) Now, build a function that will run your function in part (b), 1, 000 times and store 
#the means in a list.
def generate_1000_means(): 
    
    means = [] 
    for i in range(0,1000):
        means.append(generate_mean_x())
    return means


# In[229]:


# (d) Create a histogram of the means in the list from part (c). 
# Describe the shape of this histogram. 
#What theorem tells us that it will look the way it does?

import matplotlib.pyplot as plt 

means = generate_1000_means() 
plt.hist(means) 
plt.show()


# #### the central limit theorem tells us that it will look the way it does.
