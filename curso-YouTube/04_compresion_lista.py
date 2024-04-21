usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

# Transformación
# syntax: expression for item in items
# nombres = [usuario[0] for usuario in usuarios]

# Filtrado
#syntax: Filtrar se agrega condicional
nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Filtra y transformada
#syntax: Filtrar se agrega condicional
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]


print(nombres)