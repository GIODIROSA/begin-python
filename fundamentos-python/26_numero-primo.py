"""
Verificador de números primos: Escribe una función llamada es_primo que tome un número entero positivo 
como parámetro y devuelva True si el número es primo, y False si no lo es.

 """

numero = 7

def es_primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, numero):
       
        if numero % i == 0:
            return False
    return True
     
print(es_primo(numero))