#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random   #Importing module


# In[5]:


min_value = 1   #Initializing variables
max_value = 6
roll = "yes"


# In[ ]:


while roll == "yes":    #loop
    print("Rolling the dice")
    print("The values are")
    print(random.randint(min_value, max_value))
    print(random.randint(min_value, max_value))
    roll = input("Want to roll again")   #if yes then dice will roll again


# In[ ]:




