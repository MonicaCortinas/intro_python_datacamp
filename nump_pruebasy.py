import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
print(height)
np_height = np.array(height)
print(np_height)

weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_weight = np.array(weight)

print(weight)
print(np_weight)



print(np_weight / np_height**2)

## Diferencias entre objetos

python_list = [1, 2 ,3]
numpy_array = np.array([1, 2, 3])

print(python_list + python_list)
print(numpy_array + numpy_array)

print(np_height > 1)

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(np_baseball)
print(type(np_baseball))
