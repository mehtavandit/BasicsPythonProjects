user_input = str(input("Enter a Phrase: "))   #The string is entered by user
text = user_input.split()                     #The string gets split when white spaces occur and stores it into lis
a = " "
for i in text:
    a = a+str(i[0]).upper()                  #The index value 0 of every word is taken into consideration
print(a)                                     #Accronym is printed