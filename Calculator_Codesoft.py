#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK 2 -Codesoft

#Design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
import math

print("Enter your choice of Operation\n1. Addition(+)\n2. Subtraction(-)\n3. Multiplication(*) \n4. Division(/)\n5. Square(x2)\n6. Sqare_root(√)")

def addition(num1,num2):
    return num1 + num2

def subtraction(num1,num2):
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

def square(num):
    return num*num

def sq_rt(num):
    return math.sqrt(num)

choice=int(input())

if(choice>=1 and choice <=4):
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))

elif(choice==5 or choice ==6):
    num1=int(input("Enter number 1: "))


if(choice==1):
    add=addition(num1,num2)
    print("\nAddition = "+str(add))

elif(choice==2):
    sub=subtraction(num1,num2)
    print("\nSubtraction="+str(sub))
    
elif(choice==3):
    mul=multiplication(num1,num2)
    print("\nMultiplication="+str(mul))
elif(choice==4):
    div=division(num1,num2)
    print("\nDivision="+str(div))
elif(choice==5):
    power=square(num1)
    print("\nSquare= "+str(power))
elif(choice==6):
    sqrt=sq_rt(num1)
    print("\nSquare root: "+str(sqrt))
    
    
else:
    print("Invalid Choice")


# In[ ]:




