import numpy as np

myarr = np.array([3, 4, 5])                                #numpy array
print(myarr)

listArr = np.array([[1,2,3], [4,2,6], [8, 3, 5]])          #numpy array from list
print(listArr)
print(listArr.shape)
print(listArr.size)

rng = np.arange(10)                                        #a range: creates numpy array from 0 to n-1
print(rng)

lspace = np.linspace(1, 10, 4)                             #returns linerarly/equally spaced elements between two numbers
print(lspace)                                              #4 equally spaced numbers b/w 1 and 10.

emp = np.empty((2,3))                                      #returns empty array of given size
print(emp)

emp_like = np.empty_like(listArr)                          #returns array of same size as the input array with random nos
print(emp_like)

ide = np.identity(4)                                       #returns identity matrix of size 4
print(ide)

arr = np.arange(21)
print(arr)
print(arr.reshape(3, 7))                                   #returns sized array
print(arr.ravel())                                         #undoes 
