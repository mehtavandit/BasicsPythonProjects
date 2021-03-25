#!/usr/bin/env python
# coding: utf-8

# In[1]:


from forex_python.converter import CurrencyRates   #Importing modules


# In[2]:


c = CurrencyRates()


# In[3]:


amount=int(input("Enter the amount")) #User input 


# In[4]:


from_currency = input("From Currency: ").upper()  #Which currency you want to convert


# In[5]:


to_currency = input("To Currency: ").upper()   #To which currency you want to convert


# In[6]:


print(from_currency, " To ", to_currency , amount )


# In[7]:


result = c.convert(from_currency, to_currency, amount)   #Converting


# In[8]:


print(result)


# In[ ]:




