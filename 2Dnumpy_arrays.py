

# Import numpy
import numpy as np

#ndimensional arrays más de una dimensión

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79], [65.4, 59.2, 63.6, 88.4, 68.7]]) 
                 
print(type(np_2d))
print(np_2d)
print(np_2d.shape)

print(np_2d[0][2])
print(np_2d[0,2])

# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]


# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

import pandas as pd

df = pd.ExcelFile("baseball.xlsx")
data = df.parse("baseball")
print(data.head(10))

print(type(data))

height_in = data["Height(inches)"]
print(height_in)
print(type(height_in))

weight_lb = data["Weight(pounds)"]
print(weight_lb)
print(type(weight_lb))

baseball = [height_in, weight_lb] 

print(baseball)
print(type(baseball))

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

# Print out the 50th row of np_baseball
print(np_baseball[:,50])


# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[1,:]

# Print out height of 124th player

print(np_baseball[0,124])

print(np.mean(np_baseball[0,:]))
print(np.median(np_baseball[1,:]))
print(np.corrcoef(np_baseball[0,:], np_baseball[1,:]))



