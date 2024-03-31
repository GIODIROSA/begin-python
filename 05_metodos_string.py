# Metodo string
# método es una función que se encuentra dentro de un objeto

animal = " chanCHito feliz "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize()) #se puede encadenar metodos
print(animal.title()) #la primera y segunda como titulo
print(animal.strip()) # remueve los espacios del comienzo y final
print(animal.rstrip()) # quita espacio a la derecha
print(animal.lstrip()) # quita los espacios de la izquierda
print(animal.find("CH")) # Devuelve numero en la posición en que esta lo que se busca entre parentesis // devuelve el indice
print(animal.find("cH")) # Devuelve -1 si no encuentra
print(animal.replace("nCh", "j")) # Busca el primero y el con el segundo argumente remplaza al primero // si o si dos argumento
print("nCH" in animal) # Devuelve un boobleano // si se encuentra o no
print("nCh" not in animal) # Busca si esta cadena de caracter no se encuentra en la variable

