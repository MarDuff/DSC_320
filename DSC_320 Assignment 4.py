#!/usr/bin/env python
# coding: utf-8

# ## Calculating Limits Numerically

# In[5]:


#import libraries
import math


# In[4]:


# Let f(x) = 2x^3 − 4x + 1 and let g(x) =( e^x )− 1/ x
# (a) Use Python code to evaluate the function f at appropriate values to calculate lim f(x). Hint: Evaluate x→3
# f at values closer and closer to 3 and see what value the outputs get close to.

def f(x):
    return (2 * (x**3)) - (4 *x) + 1

for n in range(33):
    x = n/10
    print(x, f(x))


# In[29]:


# (b) Use Python code to evaluate the function g at appropriate values to calculate lim g(x).

#g(x) = (e^x − 1)/ x
def g(x):
     return (math.e**x-1)/x


for n in range(1,10):  # (0-10)
    x = 1/n
    print(round(x,2),g(x))

print(g(1/10)) 
#g(0) is undefined SO we can conclude ) is not in the domaine of the function g.
print (g(-1/10))


# ## Average Rate of Change

# In[ ]:


#AverageRateofChange (aroc) =f(b)−f(a)/b-a

#Create a Python function that takes in a mathematical function, e.g., f(x) = 3x^2 and two numbers a and b
and returns the average rate of change of the function between a and b.


# In[49]:


def f2(x):
    return 3 * (x**2)

def aroc(fn,a,b):
    return (fn(b) - fn(a)) / (b-a)

aroc(f2,10,20) #for a=10 and b=20


# ## Average Rate of Change to Instantaneous Rate of Change

# In[55]:


#A baseball is dropped from a tall cliff.
#Neglecting air resistance, the distance traveled by the baseball in meters after 
#t seconds is given by the function
#f(t) = 4.9t^2.

def f3(t):
    return 4.9 * (t**2)


# In[50]:


# (a) Find the average speed (average rate of change of distance) 
#of the baseball between 5 and 6 seconds.
print(aroc(f3,5,6))


# In[51]:


# (b) Find the average speed (average rate of change of distance) of the baseball between 5 and 5.5 seconds.
print(aroc(f3,5,5.5))


# In[52]:


# (c) Find the average speed (average rate of change of distance) of the baseball between 5 and 5.1 seconds.
print(aroc(f3,5,5.1))


# In[53]:


#(d)What is the instantaneous speed of the baseball at t = 5 seconds?
print(aroc(f3,5,5.000001))


# In[48]:


#(e) Find the derivative of f . 
#Hint: The derivative of a quadratic function f (x) = ax^2 + bx + c is given by
#f'(t) = 2ax + b

def fprime(t):
    return 2*4.9*t


# In[56]:


#(f) Evaluate the derivative of f at t = 5. 
#How does this value compare to the value found in part (d)?
#Explain what is happening

print (fprime(5)) 

# this value is obviously the same as the one calculated in part (d) cause
#it is considered as the instantaneous velocity at 5 seconds.


# ## Calculating and Interpreting Partial Derivatives

# In[57]:


#P =16000+(2400*C)−(1800*Y)


# In[69]:


#(a) What is this model’s predicted selling price of a 5-year old car with a 
#condition rating 8?
def P(x):
        return 1600 + (2400*C) - (1800*Y)

#don't really know how to run with 2 different parameters.
    
#print the function by replacing the paramters years and condition ration directly in the formula.
print((1600+ (2400*8) - (1800*5)))


# In[74]:


#(b) Find ∂P/∂C and interpret this value. 
∂P/∂C= 2400+1600


# In[75]:


#(c) Find ∂P/∂Y and interpret this value.
∂P/∂Y= -1800+1600


# In[ ]:




