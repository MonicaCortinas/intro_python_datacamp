fam = [1.73, 1.68, 1.71, 1.89]
print(max(fam)) #built-in function
tallest = max(fam)
print(tallest)

print(round(tallest, 1)) # variable, precision
print(round(tallest))
help(round)
print(round(tallest, -1))

# Create variables var1 and var2
var1 = [1, 2, 3]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

# Methods are functions that "belong" to objects

fam = ['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]

print(fam.index("mom")) #index es el método que pertenece al objeto mom

sister = "liz"

print(sister.capitalize())

#Each object has his own methods

fam.append(1.79)

print(fam)

# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place, place_up)

# Print out the number of o's in place
print(place.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.5))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)