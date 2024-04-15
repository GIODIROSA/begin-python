"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""

numeros_ganador_loteria= []
for numero in range(1, 6):
    numero_loteria= input("Ingresar los numeros de la loteria: ")
    numeros_ganador_loteria.append(numero_loteria)
    numeros_ganador_loteria.sort()
   

print(numeros_ganador_loteria)


