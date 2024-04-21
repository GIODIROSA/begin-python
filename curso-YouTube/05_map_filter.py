usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# Mapear
# nombres = list(map(lambda usuario: usuario[0], usuarios))

#Filter
menos_usuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menos_usuarios)