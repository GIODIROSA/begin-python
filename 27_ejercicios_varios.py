
"""
Suma de números pares en una lista de números
"""
   

def lista_numeros():
    acumulador= 0
    for numero in range(1, 101):
        if numero % 2 == 0:
            acumulador += numero
      
    return [acumulador]


print(lista_numeros())