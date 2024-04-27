
"""
    Escribe una función que tome una cadena como entrada y cuente cuántas palabras contiene.
"""

#planificando
# palabra = "palabra para todos"
# array_palabra = palabra.split()
# print(len(array_palabra))

texto= input("Por favor, ingrese una oración: ")

def contador_palabra(texto):
    array_texto = texto.split()
    return print(len(array_texto))


contador_palabra(texto)