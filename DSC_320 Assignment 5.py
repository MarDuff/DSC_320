#!/usr/bin/env python
# coding: utf-8

# ### Riemann Sum Function

# In[15]:


#import libraries
import math
import numpy as np
import matplotlib.pyplot as plt


# In[1]:


# Rn =f(a+Δx)Δx+f(a+2Δx)Δx+···+f(a+nΔx)Δx=Sumf(a+kΔx)Δx,
#with Δx = (b−a)/n

#Write a Python function to take in a mathematical function f, 
#two interval endpoints a and b, and the number of rectangles n, 
#and then outputs the right Riemann sum Rn.


# In[5]:


def f(x):
    return math.sqrt(4 - x**2)

def riemann_sum(f, a, b, n):

    Δx = (b-a)/n
    rs = 0
    
    for k in range(1, n+1):
        rs += f(a+k*Δx) * Δx

    return rs
    


# ### Using the Right Riemann Sum to Find the Area Under a Curve

# In[9]:


#Letf(x)= sqrt(4−x2).
#(a) Sketch a graph of f and the rectangles that make up the 
#right Riemann sum R4 on the interval [0, 2]. This can be done by hand.
#(b) Use the function you created in the previous problem to calculate R4.


# In[11]:


print(f(0))
print(f(0.5))
print(f(1))
print(f(1.5))
print(f(2))


# #### a graph  of f and the rectangles is drawn by hand and published under the assignment link.

# In[8]:


R4 = riemann_sum(f,0,2,4)
print(R4)


# In[25]:


#(c) The area below the curve of a continuous function f on the interval [a, b] 
#can be found by calculating
#what is called the definite integral of f over [a, b]. 
#The definite integral R b f (x) dx can be calculated a
#with the following limit Zb
#f(x)dx = Area Under the Curve = lim Rn. a n to ∞
#Calculate appropriate right Riemann sums to find the area under the curve 
#y = f(x) on the interval [0, 2]. Does the value of this area have a special name?


print(riemann_sum(f,0,2,10))


# In[26]:


print(riemann_sum(f,0,2,100))


# In[27]:


print(riemann_sum(f,0,2,1000))


# conclusion
# The symbol integral sign refers to the sum of an infinite number of slices. 
# Each value calculated is slice area. 
