"""

Contador de vocales: Escribe una función llamada contador_vocales que tome una cadena como parámetro y devuelva un diccionario con la cantidad de cada vocal (a, e, i, o, u) en la cadena.
    
"""

def contador_vocales(texto):
    vocales= ""
    for letra in texto:
        if letra.lower() in "aeiou":
            vocales += letra

    diccionario = ",".join(vocales)
    return {diccionario}   
           

resultado_diccionario = contador_vocales("loquesea")
print(resultado_diccionario)

