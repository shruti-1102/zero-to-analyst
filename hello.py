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
m = {"name" : "John", "age" : 36}	             #dict	
n = {"apple", "banana", "cherry"}	             #set	
o = frozenset({"apple", "banana", "cherry"})	 #frozenset	
p = True	                                     #bool

print(random.randrange(1, 100))

q = "I'm learning python."
print(q[4])
print(len(q))
print("Python" in q)
if "python" in q:
    print("Yes, python is present!!")
print(q[2:9])                                   #slicing
