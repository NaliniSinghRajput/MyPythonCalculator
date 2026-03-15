#!/usr/bin/env python
# coding: utf-8

# In[1]:


#### print("Please make a choice from 1 to 6")
def Sum(a,b):
    result = a + b
    return result

def Difference(a,b):
    result = a - b
    return result

def Multiplication(a,b):
    result = a * b
    return result

def Division(a,b):
    result = a/b
    return result

def Power(a,b):
    result = a ** b
    return result

def function(a,b):
    result = (a+b)**2
    return result


print("Hello and welcome to my calculator!, you have the following operations to choose from:")
print("1.Sum")
print("2.Difference")
print("3.Multiplication")
print("4.Division")
print("5.Power")
print("6.(a + b)**2")

choice = input("Enter a number from 1 to 6: ")

a = float(input("Please enter the number a: "))
b = float(input("Please enter the number b: "))

if choice == "1":
    print("Result : ", Sum(a,b))
elif choice == "2":
    print("Result : ", Difference(a,b))
elif choice == "3":
    print("Result: ", Multiplication(a,b))
elif choice == "4":
    print("Result: ", Division(a,b))
elif choice == "5":
    print("Result: ", Power(a,b))
elif choice == "6":
    print("Result: ", function(a,b))


# In[ ]:




