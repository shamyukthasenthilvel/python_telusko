import numpy as np
arr1=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr1)
print(arr1.ndim)
print(arr1.dtype)
print(arr1.size)
arr2=arr1.flatten()
print(arr2)
arr3 =np.array([ 
    [1,2,3,4,56,48],
    [5,6,7,8,9,87]
])
arr4=arr3.reshape(3,4)
print(arr4)
arr6 =np.array([ 
    [1,2,3,4,56,48],
    [5,6,7,8,9,87]
])
arr5 = arr6.reshape(2,2,3)
print(arr5)