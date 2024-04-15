
# 3. Desarrolle un script que a través de una función que recibe una palabra, retorne como respuesta si la palabra ingresada por
# teclado es o no Palíndromo:

def esPalindromo(palabra):
    palabra= palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

palabra_ingresada = input("Ingrese una palabra: ")

if esPalindromo(palabra_ingresada):
    print("Es un Pálindromo")
else:
    print("No es un Pálindromo")
    




