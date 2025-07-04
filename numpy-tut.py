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
print(arr.ravel())                                         #flattens the array 

x = [[1,2,3], [4,5,6], [7,1,0]]
ar = np.array(x)
print(ar)
print(ar.sum(axis=0))                                      #axis=0 -> column wise sum. [1+4+7, 2+5+1, 3+6+0]
print(ar.sum(axis=1))                                      #axis=1 -> row wise sum. [1+2+3, 4+5+6, 7+1+0]

print(ar.T)                                                #TRANSPOSE the array

for item in ar.flat:                                       #1D iterator over all elements in any N-D array.
    print(item)

print(ar.ndim)                                             #returns the number of dimensions
print(ar.size)                                             #returns the number of elements

one = np.array([1, 23, 452, 45, 3, 10])
print(one.argmax())                                        #returns the index where largest element is present
print(one.argmin())                                        #returns the index where min element is present
print(one.argsort())                                       #returns array of indices where elements get sort

two = np.array([[1,2,3], [4,5,6], [7,1,0]])
print(two.argmax())                                        #straightens the array then finds the maximum element
print(two.argmin())                                        #opposite of argmax
print(two.argmax(axis=0))                                  #returns the array containing sorted indices in 0 axis
print(two.argmax(axis=1))                                  #returns the array containing sorted indices in 1 axis
print(two.argsort(axis=1))                                 #returns the matrix containing sorted indices

thr = np.array([[1,2,1], [4,0,6], [8,1,0]])

print(two+thr)                                             #numpy let's us do arithematic matrix operations
print(two*thr)
print(np.sqrt(two))
print(two.sum())
print(two.max())
print(two.min())

print(np.where(two>5))                                     #returns array of indices where the condition is true.
print(np.count_nonzero(two))                               #returns the count of the elements that are not zero

arr = np.array([1, 2, 3, 4, 5])
print(arr[::2])

arr = np.arange(10)
print(arr.reshape(2, 5).shape)
