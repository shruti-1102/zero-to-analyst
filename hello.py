# 🔰 Python Basics Practice - Shruti Singh Parihar
# Covers: Variables, Data Types, Strings, Lists, Functions, f-strings, Random, etc.
# Date: June 2025
# Purpose: To revise core Python needed before diving into data analysis

import random

print("Hello World!")
a = 5
b = 4
print(a+b)
print(type(a))

d, e, f = "Shruti", "Singh", "Parihar"
print(d, e, f, "is my name")

g = h = i = "Parrot"
print(g)
print(h)
print(i)

def myFuc():
    a = "Shuru"
    print(a)
myFuc()
print(a)

j = ["apple", "banana", "cherry"]	             #list	
k = ("apple", "banana", "cherry")	             #tuple	
l = range(6)	                                 #range	
m = {"name" : "John", "age" : 36}	             #dictionary	
n = {"apple", "banana", "cherry"}	             #set	
o = frozenset({"apple", "banana", "cherry"})	 #frozenset	
p = True	                                     #bool

print(random.randrange(1, 100))

q = " Yes, I'm learning python."
print(q[4])
print(len(q))
print("Python" in q)
if "python" in q:
    print("Yes, python is present!!")
print(q[2:9])                                     #slicing
print(q[:10])                                     #slice from the start
print(q[-15:-2])                                  #negative slicing

print(q.upper())                                  #built in upper case method
print(q.lower())                                  #lower case method
print(q.strip())                                  #removes extra space before or after the text
print(q.replace("p", "P"))                        #replaces string
print(q.split(","))                               #splits the string

r = "Hey"
s = "you"
print(r + " " + s)                                #string concatenation

age = 22
text = f"Hey, my name is Shruti and I'm {age}"    #f strings
print(text)

price = 59
txt = f"The price is {price:.2f} dollars"         #MODIFIER .2f means fixed point number with 2 decimals
print(txt)

print(isinstance(age, int))                       #inbuilt function to determine datatype

print(x:=3)                                       #operator := x = 3, print(x)

myList = ["apple", "banana", "lychee"]            #list
print(myList)                                     #allows duplicate items
myList.append("apple")                            #method used to add in the end
print(myList)
print(len(myList))                                #length of the list
myList.append(True)                               #to add item at the end
myList.append(4)                                  #can contain different data types
myList.insert(1, "blueberry")                     #to insert item at specific position
print(myList)
print(type(myList))
print(myList[2])                                  #indexed items, positive & negative
print(myList[2:5])                                #range of indexes allowed

if "lychee" in myList:
    print("Yes, lychee is added in the list.")
myList[1] = "mango"
print(myList)                

myList2 = [4, "Shruti", "file", "code"]
myList.extend(myList2)                            #append items from another list
print(myList)
myList.remove("file")                             #remove any item from the list
myList.pop(6)                                     #remove item from specific index
print(myList)
