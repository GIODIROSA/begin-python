


texto_usuario = input("Ingresar un texto: ")
letras_minuscula = "aeiou"
contador= 0

""" 
recorrer cada letras y parsearlas
evaluar la vocal a e i o u 
debe contar
mostrar la cantidad total de vocales
""" 


def contador_vocales(texto):
    vocales = ""
    for letra in texto:
        if letra.lower() in letras_minuscula:
            vocales += letra
    contador = len(vocales)
    return print(f"las vocales son: {vocales} y la cantidad de vocales es: {contador}")
            
            
            
contador_vocales(texto_usuario)

