# 2. Desarrolle un script que a través de una función tome una cadena de texto como argumento y cuente la cantidad de veces
# que aparece cada palabra en la cadena. Debe retornar un diccionario donde las claves son las palabras y los valores son las
# cantidades de veces que conto a la palabra:


def contarPalabra(cadena):
    palabras = cadena.split()
    contador = {}

    for palabra in palabras:
        palabra = palabra.lower()

        if palabra in contador:
            contador[palabra] += 1
        else: 
            contador[palabra] = 1
            
    return contador


oracion = "La maquina dentro de la maquina funciona de manera mecanica dentro de la maquina"

resultado = contarPalabra(oracion)

print("=>", resultado)