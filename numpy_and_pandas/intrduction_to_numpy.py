# Q1 Create a two dimension 3*3 array and perform ndim, shape and slicing on it.

import numpy as np
array = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])

print("Dimension of the array- ", array.ndim)
print("number of element in the array- ", array.shape)
print("slicing on the array-")
print(array[0:2 , 0:2])


# Q2 Create a one dimension array and perform ndim, shape and reshape operation  on it.

import numpy as np
array = np.random.randint(0, 50, 9)
print(array)
print("Dimension of the array- ", array.ndim)
print("number of element in the array- ", array.shape)
new_array = array.reshape(3,3)
print(new_array)
print("Dimension of the new array- ", new_array.ndim)
print("number of element in the new array- ", new_array.shape)

