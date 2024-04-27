"""
Suma de números pares: Escribe una función llamada suma_pares que tome un número 
entero positivo n como parámetro y devuelva la suma de todos los números pares desde 1 hasta n.
"""

entero_positivo = 4

def suma_pares(numero_entero):
    suma_de_pares = 0
    for numero in range(1, numero_entero+1):
        if numero % 2 == 0: 
            suma_de_pares += numero
            print(suma_de_pares)
    
          
      
suma_pares(entero_positivo)


