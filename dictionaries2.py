world = {"afghanistan": 30.55, "albania":2.77, "algeria": 39.21}
print(world["albania"])

# Las claves no pueden repetirse

world = {"afghanistan": 30.55, "albania":2.77, "algeria": 39.21, "albania":2.81}
print(world["albania"])

# Keys tienen que ser "inmutable objects"

# Para añadir cosas, se añaden con igual

world["sealand"] = 0.000027
print(world)

"sealand" in world

# Se pueden cambiar los valores

world["sealand"] = 0.000028

print(world)

# para borrar

del(world["sealand"])

print(world)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe["italy"] = "rome"

# Print out italy in europe
print(europe["italy"])

# Add poland to europe
europe["poland"] ="warsaw"

# Print europe
print(europe)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe["germany"] = "berlin"

# Remove australia
del(europe["australia"])

# Print europe
print(europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe["france"]["capital"])


# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

