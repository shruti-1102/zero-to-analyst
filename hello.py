# 🔰 Python Basics Practice - Shruti Singh Parihar
# Covers: Variables, Data Types, Strings, Lists, Functions, f-strings, Random, etc.
# Date: June 2025
# Purpose: To revise core Python needed before diving into data analysis

import random
import os

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

j = ["apple", "banana", "cherry"]	              #list	
k = ("apple", "banana", "cherry")	              #tuple	
l = range(6)	                                  #range	
m = {"name" : "John", "age" : 36}	              #dictionary	
n = {"apple", "banana", "cherry"}	              #set	
o = frozenset({"apple", "banana", "cherry"})	  #frozenset	
p = True	                                      #bool

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
print(q.replace("p", "P"))                        #replaces strings
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
myList.pop(5)                                     #remove item from specific index
myList.pop(5)
myList.pop(5)
print(myList)

myList3 = [x for x in myList if "p" in x]         #List comprehension
print(myList3)

myList4 = [2, 56, 3, 8, 5, 12, 87]
myList4.sort()                                    #sorting in ascending order
print(myList4)
myList4.sort(reverse=True)                        #reversing a list
print(myList4)

myTuple = ("apple", "mango", "banana")            #tuple

thisTuple = ("apple",)                            #tuple with one item.
print(type(thisTuple))
thisTuple2 = ("apple")                            #string
print(type(thisTuple2))

myTup = ("apple", "mango", "banana")              #how to change an item in a tuple
myTup2 = list(myTup)
myTup2[1] = "kiwi"
myTup = tuple(myTup2)
print(myTup)

fruits = ("apple", "banana", "cherry")            #multiply tuples
mytuple = fruits * 2
print(mytuple)

mySet = {"apple", "mango", "banana"}              #set
mySet.add("lychee")
print(mySet)

mySet2 = {"a", "b", "c"}
mySet.update(mySet2)
print(mySet)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)                           #all items in both
print(set3)

set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set6 = set4.intersection(set5)                    #only common items
print(set6)

thisdict = {                                      #dictionary
  "brand": "Ford",                                #key-value pairs
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict.get("model"))
print(thisdict.keys())

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x)
car["color"] = "white"                            #add a key value pair
print(x)
y = car.values()
print(y)

def myFunc(fname):                                #function
    print("Welcome", fname)

myFunc("Shruti")


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

aaa = 3                                           #comment this line to catch the error
try:                                              #exceptional handling
    print(aaa)
except:
    print("An error occured")


f = open("myFile.txt")                            #file handling
print(f.read())
f.close()

with open("myFile.txt") as f:
#    print(f.read())                              #read the whole file
   print(f.readline())                            #only read one line


with open("myFile.txt", "a") as f:                #writing into file
   f.write("Add more content to the file")

with open("myFile.txt") as f:
   print(f.read())

with open("myFile.txt", "w") as f:                #overwrite existing content
   f.write("Old content deleted!")

with open("myFile.txt") as f:
   print(f.read())

os.remove("myFile.txt")