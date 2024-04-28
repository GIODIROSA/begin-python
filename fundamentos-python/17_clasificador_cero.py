# Clasificador de números: Solicitar al usuario 5 números y clasificarlos en positivos, negativos o cero.

numero_uno= int(input("Ingresar el numero uno: "))
numero_dos= int(input("Ingresar el numero dos: "))
numero_tres= int(input("Ingresar el numero tres: "))
numero_cuatro= int(input("Ingresar el numero cuatro: "))
numero_cinco= int(input("Ingresar el numero cinco: "))

numeros= [numero_uno, numero_dos, numero_tres, numero_cuatro, numero_cinco]
    
print("=>", numeros)

def clasificarNumero (numeros):
     for numero in numeros:
         if numero == 0:
            print("El numero es cero: ", numero)
         elif numero > 0:
            print("El numero es positivo: ", numero)
         else:
            print("El numero es negativo: ", numero)
            

print("=>", clasificarNumero(numeros))


# numero == 0
# numero es CERO
# sino  
# numero > 0
# positivo
# else
# numero es negativo








