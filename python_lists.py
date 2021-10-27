# Una lista
lista = [1.73, 1.68, 1.71]
print(lista)

# Distintos elementos
['liz', 1, 'emma']

# Sublistas
fam2 = [['liz', 1.73], ['emma', 1.62]]

print(fam2)
print(type(fam2))

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# Adapt list areas
areas = ["hallway", hall,"kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas

# Print areas
print(areas)

#subsetting list (0 indexing)
print(areas[0])
print(areas[-1]) # el último
print(areas[3:5]) #[start including:end excluding]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)

# Use slicing to create downstairs
downstairs = areas[:6]
print(downstairs)
# Use slicing to create upstairs
upstairs = areas[-4:]
print(upstairs)
# Print out downstairs and upstairs

print(downstairs, upstairs)

# Changing lists
upstairs[0] = "nuevo"
print(upstairs)

# Para borrar podemos usar del()

# Correct the bathroom area
areas[-1] =10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"

print(areas)

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 14.45]

print(areas_2)


# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

del(areas[10:11])

print(areas)