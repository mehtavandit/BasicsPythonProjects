#!/usr/bin/env python
# coding: utf-8

# In[9]:


from forex_python.converter import CurrencyRates   #Importing modules
c = CurrencyRates()
amount=int(input("Enter the amount")) #User input 
from_currency = input("From Currency: ").upper()  #Which currency you want to convert
to_currency = input("To Currency: ").upper()   #To which currency you want to convert
print(from_currency, " To ", to_currency , amount )
result = c.convert(from_currency, to_currency, amount)   #Converting
print(result)

