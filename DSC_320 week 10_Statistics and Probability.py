#!/usr/bin/env python
# coding: utf-8

# ### 1. Summarizing Data

# In[3]:


#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


df1=pd.read_csv('qb_stats.csv')
df1.head()


# In[11]:


df1.shape


# ##### (a) Find the mean of each numerical column of data.
# #####  (b) Find the standard deviation of each numerical column of data.

# In[15]:


df1.describe()


# ##### (c) Create a histogram of the number of yards; label it appropriately.

# In[20]:


hist = plt.hist(df1['yds'],density=True)
plt.xlabel("yards")


# ##### (d) Create a boxplot of the number of touchdowns. Identify any outliers.

# In[21]:


plt.boxplot(df1['td'])
 
plt.show()


# In[14]:


def find_outliers_IQR(df1):

   q1=df1.quantile(0.25)

   q3=df1.quantile(0.75)

   IQR=q3-q1

   outliers = df1[((df1<(q1-1.5*IQR)) | (df1>(q3+1.5*IQR)))]

   return outliers


outliers = find_outliers_IQR(df1['td'])

print('number of outliers: '+ str(len(outliers)))

print('max outlier value: '+ str(outliers.max()))

print('min outlier value: '+ str(outliers.min()))

outliers


# ### 2. Calculating Probabilities from Data

# In[6]:


#import data
df2= pd.read_csv('survey_data.csv')
df2.head()


# In[37]:


df2.shape


# In[25]:


df2.describe()


# ##### (a) Based off of this data, what is the probability a college student has brown hair?
# ##### (b) Based off of this data, what is the probability a college student has blue eyes?
# ##### (c) Based off of this data, what is the probability a college student has blue eyes given that they have brown hair?
# ##### (d) Based off of this data, what is the probability a college student has brown hair given that they have blue eyes?
# ##### (e) Do your results above indicate that college students having brown hair and blue eyes are inde- pendent of one another? Explain.

# In[26]:


#calculate probablities

#a)
val_counts = df2['eye_color'].value_counts()
blue_eyes = df2['eye_color'].value_counts()["blue"]
print(blue_eyes)
      
prob_blue_eyes = blue_eyes/df2.shape[0]
print("Probability of blue eyes:",prob_blue_eyes)



# In[27]:


#b)
value_counts= df2['hair_color'].value_counts()
print(value_counts)
probability_Brown_hair= value_counts['brown']/df2.shape[0]
print("Probability of brown hair:",probability_Brown_hair)


# In[12]:


#c)
# Idea 1:
# Count rows with brown hair.
BH_values= df2['hair_color'].value_counts()['brown']

print('Brown hair count:',BH_values)

# Count rows with both brown hair and blue eyes.
blue_eyes=df2['eye_color'].value_counts()["blue"]
print('Blue eyes count:',blue_eyes)

BH_and_BE_values= BH_values+blue_eyes

print(BH_and_BE_values)

# Divide the latter by the former.
probability_BH_BE= BH_and_BE_values/df2.shape[0]
print(probability_BH_BE)


# In[13]:


#d)
probability_BH_BE= BH_and_BE_values/df2.shape[0]
print(probability_BH_BE)


# In[43]:


#(f) Create a bar graph of the hair color and eye color of this group of students. 
#Label the graphs appropriately.

import matplotlib.pyplot as plt


plt.hist(df2['hair_color'], density=True)
 
plt.xlabel('hair_color')


# In[40]:


plt.hist(df2['eye_color'],density=True)
plt.xlabel('eye color')

