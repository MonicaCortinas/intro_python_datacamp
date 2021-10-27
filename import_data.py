import pandas as pd

df = pd.ExcelFile("baseball.xlsx")
data = df.parse("baseball")
print(data.head(10))

print(type(data))

height_in = data["Height(inches)"]
print(height_in)
print(type(height_in))

weight_lb = data["Weight(pounds)"]

# Import numpy
import numpy as np
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = 0.0254 * np_height_in

# Print np_height_m
print(np_height_m)

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

# Calculate the BMI: bmi

bmi = np_weight_kg / np_height_m**2

# Print out bmi
print(bmi)

# Create the light array
light = bmi < 21

# Print out light
print(light)

print(bmi[light])