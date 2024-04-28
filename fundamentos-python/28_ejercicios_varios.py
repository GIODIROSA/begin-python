
"""
Escribe una función que tome un número como entrada y muestre la tabla de multiplicar de ese número del 1 al 10.    
"""


def multiplicar(numero):
 
    for multiplo in range(1 , 11):
        resultado = numero * multiplo
        print(f"{numero} x {multiplo} = {resultado}")
      
    

multiplicar(3)