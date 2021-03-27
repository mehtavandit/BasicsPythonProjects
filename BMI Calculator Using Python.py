#!/usr/bin/env python
# coding: utf-8

# In[4]:


Height = float(input("Enter your height in cm"))/100  #User inputing Height
Weight = float(input("Enter your weight in kg"))      #User inputing Weight
BMI = Weight/(Height**2)                              #Calculating BMI
print("Your Body Mass Index is", BMI)

if(BMI>0):                                            #Your Health Status
    if(BMI<=18.5):
        print("You are underwight")
    elif(BMI<=25):
        print("You are Healthy")
    elif(BMI<=30):
        print("You are overweight")
    else:
        print("You are severely overweighted")
else:
    print("Enter valid details")

        

