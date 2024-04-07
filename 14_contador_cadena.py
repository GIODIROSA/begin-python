


# 1. Desarrolle un script que a través de una función una cadena de caracteres y muestre como resultado dos cadenas, una que contenga solo las vocales y otra solo las consonantes


def separador_cadena(palabra):
    vocales= ""
    consonantes= ""

    for letra in palabra:
        if letra.lower() in "aeiou":
            print("vocales", letra)
            vocales += letra
        else:
            print("consonante:", letra)
            consonantes += letra
    return vocales, consonantes

            
palabra = (input("Ingrese una palabra y luego presione ENTER: "))

vocales_resultado, consonantes_resultado = separador_cadena(palabra)

print("vocales: ", vocales_resultado)
print("consonantes: ", consonantes_resultado)


