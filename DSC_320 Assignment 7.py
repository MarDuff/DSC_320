#!/usr/bin/env python
# coding: utf-8

# ### Working with Matrices

# In[40]:


#import libraries
import numpy as np
import pandas as pd


# ##### Let A, B, and C be the given matrices

# ##### 1. Enter each of the matrices A, B, and C as Numpy matrix.

# In[20]:


A =np.array([[1, -2, 3, 7],
            [2, 1, 1, 4], 
            [-3, 2, -2, 10]])

B= np.array([[0, 1, -3, -2],
           [10, -1, 2, -3],
           [5, 1, -1, 4]])

C= np.array([[4, 0, -2, 3],
           [3, 6, 9, 7],
           [2,2,5,1],
           [9, 4, 6, -2]])



# ##### 2. What are the dimensions of each of the matrices A, B, and C? Display these using Python code.
# 

# In[26]:


print("DimA: ", A.ndim)
print("DimB: ", B.ndim)
print("DimC: ", C.ndim)


# ##### 3. Determine if each of the following matrix operations is defined. If it is defined, calculate the result using Python. If it is not defined, explain why it is not defined.
# (a) A+B ,
# (b) AB ,
# (c) AC ,
# (d) C^T

# In[27]:


#Addition
A + B


# In[30]:


#matrices multiplication
A*B


# In[31]:


A*C


# In[32]:


C.T


# ##### 4. Illustrate the following property of matrix transpositions using these matrices: (A + B)T = AT + BT .
# 

# In[33]:


(A+B).T


# In[34]:


(A.T)+ (B.T)


# In[35]:


(A+B).T==A.T+B.T


# ##### 5. Illustrate the following property of matrix transposition using these matrices (AC)T = CT AT .
# 

# In[36]:


(A*C).T


# In[37]:


(C.T)* (A.T)


# In[39]:


(A*C).T==(C.T)*(A.T)
#This operation can not be made because the two matrices have different shapes.


# ##### Fine C−1 using Python code.

# In[38]:


C_inv = np.linalg.inv(C)
C_inv


# ### Working with Images

# ##### 1. Use the following code to display the image.
# 

# In[49]:


#import the OpenCv library to read images
import cv2
#import martplotlib to display the image
import matplotlib.pyplot as plt

#import the image; by default, OpenCV impports images in the BGR format
image_bgr = cv2.imread('week7_image.jpg', cv2.IMREAD_COLOR) 

#convert the image to the RGB formate
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

#display the image pIt.imshow(image_rgb)
plt.axis ("off")
plt.show


# ##### 2. Find the resolution of this image. Hint: OpenCV imports the image as a Numpy array, where each pixel corresponds to an entry in the array.

# In[62]:


image= cv2.imread('week7_image.jpg')


# In[66]:


image.shape


# In[69]:


wid = image.shape[1] 
hgt = image.shape[0] 
  
# displaying the dimensions 
print(str(wid) + "x" + str(hgt))


# ##### 3. In checking the array dimensions, you should see that three numbers are displayed. What is this third number, and why is it there?

# ##### The shape of the image tells  that the array has three dimensions. There are 453 images and each image is 600 pixels with three colors for each pixel. This means that there are 600 *  3 = 1800 values for the image. 

# In[ ]:




