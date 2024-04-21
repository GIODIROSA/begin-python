
numeros = [1,2,3]
# print(numeros)
letras = ["a", "b", "c"]
# print(letras[2])

palabras= ["chanchito", "feliz"]
palabras_felices= ["chanchito", "felices", "felipe", "alumno"]
# print(palabras_felices)

booleans = [True, False, True, True]
# print(booleans)


matriz=[[0,1], [1,0]]
# print(matriz)

ceros =[0,1] * 10
# print(ceros)

# Concatenar Listas
alfanumerico = numeros + letras
# print(alfanumerico)

# Rango

rango = list(range(1,11))
# print(rango)

chars = list("Hola mundo")
# print(chars)

# Manipulando listas

# mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]

# mascotas[0]= "Bicho"
# print(mascotas)
# print(mascotas[0:3])
# coloca por default el indice cero
# print(mascotas[:3]) 
# print(mascotas[2:]) 
# print(mascotas[-1])
# Solo los elementos pares de una lista
# print(mascotas[::2])
# print(mascotas[1::2]) 

numeros = list(range(1,21))
numeros = list(range(21))

# print(numeros[::2])
# print("Impar", numeros[1::2])
# print("Par", numeros[::2])
# print(numeros[::3])

# Desempaquetar listas
# numeros = [1, 2, 3]
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# no importa el orden porque fue declarado de es manera al momento de desempacar
# primero, segundo, tercero = numeros

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, ultimo = numeros
# print(primero, segundo, ultimo, otros)


# Iterando listas

mascotas= ["Pelusa", "Pulga", "Felipe", "Chanchito", "Feliz"]

#creacion de tupla con "enumerate"
# for indice, mascota in enumerate(mascotas):
    # print(indice, mascota)


# Buscando elementos


animales= ["Pelusa", "Pulga", "Felipe", "Chanchito", "Feliz", "Felipe", "Felipe"]

print(animales.count("Felipe"))

if "Pulga" in animales:
    print(animales.index("Pulga"))
else:
    print("No existe el animal que se consulta")


mascotas2= ["Wolfgang", "Pelusa", "Pulga", "Felipe", "Pulga", "Chanchito", "Feliz"]

# mascotas2.insert(2, "Gabriela")
# mascotas2.append("Chanchito triste")
# mascotas2.remove("Pulga") # Elimina el primero.
mascotas2.pop(2) # eliminar el preciso del indice
del mascotas2[0]
mascotas2.clear()
# print("=>", mascotas2)


# Ordenando Listas

numeros= [2, 4, 1, 45, 75, 22]

# numeros.sort()
# numeros.sort(reverse=True)

numeros2 = sorted(numeros) # Devuelve una nueva lista
numeros2 = sorted(numeros, reverse=True) # Devuelve una nueva lista pero al reves 


print(numeros)
print(numeros2)


usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]
def ordena(elemento):
    return elemento[1]

# usuarios.sort(key=ordena)
usuarios.sort(key=ordena, reverse=True) #caso contrario

print(usuarios)
