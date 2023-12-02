#!/usr/bin/env python
# coding: utf-8

# ### 1. Calculating Probabilities using Bayes’ Theorem
# 

# #### A computer graphics card is manufactured using three different processes, A, B, and C. The following tree diagram gives the probability that a graphics card is manufactured with each process and the probability of defective and non-defective cards from each process. Use Bayes’ Theorem to calculate the following probabilities

# In[18]:


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import math

# Read Images
img = mpimg.imread('prob_tree_diagram.png')
 
# Output Images
plt.imshow(img)


# In[31]:


# (a) If a randomly chosen graphics card is defective, 
# what is the probability it was manufactured using Process A?

#To calculate this probability, we can use Bayes' Theorem:


#define function for Bayes' theorem
def bayesTheorem(pA, pB, pBA):
    return pA * pBA / pB

#P(B|A): The probability of event B, given event A has occurred.
#P(A): The probability of event A.
#P(B): The probability of event B.

#define probabilities
prob_defA= 0.3
prob_A=0.4
prob_def= 0.15

#use function to calculate conditional probability
bayesTheorem(prob_A, prob_def,prob_defA)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         


# #### the probability that a randomly chosen graphics card is defective and was manufactured using Process A is 0.8

# In[44]:


#(b) If a randomly chosen graphics card is not defective, 
#what is the probability it was manufactured using Process C?

def bayesTheorem(pC, pD, pCD):
    return pC * pCD / pD

#We can find the values of these probabilities from the tree diagram:
prob_not_defC = 0.8
prob_C= 0.5
prob_not_defective= 0.85

#Substituting these values into Bayes' Theorem, we get
bayesTheorem(prob_C, prob_not_defective,prob_not_defC)


# #### The probability that a randomly chosen graphics card is not defective and was manufactured using Process C is 0.47

# ### 2. Entropy Function for a Probability Distribution

# In[50]:


# Create a Python function that takes in an array of probabilities 
#p1, p2, . . . , pn, from a discrete prob- ability distribution 
#with n possible outcomes and returns the entropy of the corresponding 
#random variable. Use the formula on p. 143 of Essential Math for Data Science to calculate the entropy.

import math

def entropy(probabilities):
    
    #  probabilities must sum to 1
    if not math.isclose(sum(probabilities), 1.0):
        raise ValueError("Probabilities must sum to 1")
    
    # Calculate entropy
    entropy_value = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy_value

# test
probabilities = [0.5, 0.2, 0.3]
result = entropy(probabilities)
print(f"Entropy: {result}")


# ### 3. Calculating Entropies of Probability Distributions

# In[53]:


#Two random variables X and Y can take on the values 1, 2, . . . , 5 
#with the following probabilities.
#x=(1,2,3,4,5); P(X = x)=(0.2,0.2,0.2,0.2,0.2)
#y=1,2,3,4,5; P(Y = y)= (0.1,0.4,0.1,0.3,0.1)

#(a) Use the function you created in the previous problem to 
#calculate the entropies of X and Y 

probabilities = [0.2, 0.2, 0.2,0.2,0.2]
result = entropy(probabilities)
print(f"Entropy_X: {result}")

probabilities = [0.1, 0.4, 0.1,0.3,0.1]
result = entropy(probabilities)
print(f"Entropy_Y: {result}")



# In[54]:


# (b) Compare the two values found in part (a). 
#Which one is bigger? Explain intuitively why this is the case.


# #### Each of these transformed probabilities is weighted by the corresponding raw probability. The probabilities of X occur frequently, so they give more weight into the entropy of the distribution.
# #### Entropy_X > Entropy_Y
