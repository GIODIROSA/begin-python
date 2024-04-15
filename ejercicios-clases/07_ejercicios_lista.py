"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""

numeros= []

for numero in range(1,11):
    numeros.append(numero)

for item in numeros[::-1]:
        print(item)