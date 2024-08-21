"""
/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

"""

## Operaciones

s1 = "Hola"
s2 = "Python"

## CONCATENACIÓN
print(s1 + "," + s2 + "!")

## LONGITUD
frase = len(s1)
print(f"La longitud es: {frase}")

## RECORRIDO
palabra= "Piramide"

for caracter in palabra:
    print(caracter)


cadena= "Hola soy una cadena de ejemplo"
subcadena = "cadena"

posicion=(cadena.find(subcadena))

print("posicion =>", posicion)

if posicion != -1:
    print(f"La subcadena '{subcadena}' se encuentra en la posición {posicion}.")
else:
    print(f"La subcadena '{subcadena}' no se encuentra en la cadena.")

## nota: si no se encuentra en la cadena de texto te arroja un -1
cadena2= "Hola soy una cadena de ejemplo"
subcadena2 = "Python"

posicion2= (cadena2.find(subcadena2))
print(posicion2)

if posicion2 != -1:
    print(f"{subcadena2} existe en la frase: {cadena2}")
else:
    print(f"{subcadena2} no existe en la cadena: {cadena2}")

## Transformacion de string en lower/ upper/ capitalize

nombre= "giovanni"
convertir_mayuscula= nombre.upper()
convertir_minuscula = nombre.lower()
convertir_capitalize = nombre.capitalize()

print("mayuscula: ", convertir_mayuscula)
print("minuscula: ", convertir_minuscula)
print("capitalize ", convertir_capitalize)

## Repetición
frase_religiosa = "Ora pro novis"
for i in range(1,11):
    print(f"{i}.-{frase_religiosa}")


## Reemplazo

texto = ["El gato está aquí", "El perro está aquí", "El ratón está aquí"]
nuevas_frases = [frase.replace("está aquí", "se fue") for frase in texto]
print(nuevas_frases)

texto2= "Jesus esta aquí"
if "Jesus" in texto2:
    print("El está aquí")
else: 
    print("Nunca vino")

## Te separa el string y te lo convierte en lista
my_string = "Yo programo por medio de string"
print(my_string.split())

mi_cadena= "Manzana,Pera,Piña,Lechuga"
print(mi_cadena.split(','))

## Dificultad (extra)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""


def anagrama(cadena1, cadena2):
    cadena1_limpia = cadena1.lower().replace(" ", "")
    cadena2_limpia = cadena2.lower().replace(" ", "")

    """
    sorted: metodo separa y voltea de manera ascendente
    entrada: "cba"
    salida: ["a","b","c"]
    join: une todo en una sola cadena
    entrada: ["a","b","c"]
    salida: "abc"
    """

    cadena1_ordenada = "".join(sorted(cadena1_limpia))
    cadena2_ordenada = "".join(sorted(cadena2_limpia))

    return cadena1_ordenada == cadena2_ordenada



def palindromo(cadena1, cadena2):
    cadena1_limpia= cadena1.lower().replace(" ", "")
    cadena2_limpia= cadena2.lower().replace(" ", "")
    """
    [::-1] voltea la palabra
    posterior se compara cadena1 es igual a cadena2
    """
    return cadena1_limpia == cadena2_limpia[::-1]



def isograma(cadena1, cadena2):
    cadena1_limpia = cadena1.lower().replace(" ", "")
    cadena2_limpia= cadena2.lower().replace(" ", "")

    letras_unicas1= set(cadena1_limpia)
    letras_unicas2= set(cadena2_limpia)

    comparacion_cadena1= len(letras_unicas1) == len(cadena1_limpia)
    comparacion_cadena2= len(letras_unicas2) == len(cadena2_limpia)

    return comparacion_cadena1 and comparacion_cadena2



def comprobar_cadena(cadena1, cadena2):
    if anagrama(cadena1, cadena2) and palindromo(cadena1, cadena2):
        print("La palabra es una anagrama y un palindromo")
    elif isograma(cadena1, cadena2):
        print("La palabra es un Isograma")
    else:
        print("La palabra no cumple con ninguna de las opciones")


def main():
    cadena1 = input("Ingrese la primera palabra: ")
    cadena2 = input("Ingrese la segunda palabra: ")

    comprobar_cadena(cadena1, cadena2)


main();