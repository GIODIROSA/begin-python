
"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(cadena1, cadena2):
    cadena1_limpia = cadena1.lower().replace(" ", "")
    cadena2_limpia = cadena2.lower().replace(" ", "")
    
    cadena1_ordenada= "".join(sorted(cadena1_limpia))
    print("=:",cadena1_ordenada) 
    cadena2_ordenada= "".join(sorted(cadena2_limpia))  
    print("=x",cadena2_ordenada) 
     
    return cadena1_ordenada == cadena2_ordenada


cadena1 = input("Ingrese la primera palabra: ")
cadena2 = input("Ingrese la segunda palabra: ")



if anagrama(cadena1, cadena2):
    print("La palabra es una anagrama")
else: 
    print("Falso la palabra no es una anagrama")
        