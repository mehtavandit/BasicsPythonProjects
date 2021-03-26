#!/usr/bin/env python
# coding: utf-8

# In[5]:


def ip_address(address):
    new_address = ""
    splited_address = address.split(".")
    seperator = "[.]"
    new_address = seperator.join(splited_address)
    return new_address

user_input = input("Enter the ip address")       #User inputing IP Address
ip_address = ip_address(user_input)              #IP Address passed to function and defang IP Address is returned
print(ip_address)

