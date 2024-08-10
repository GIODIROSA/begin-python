"""
/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

"""

## Función simple:

def funcion_simple():
    print("Soy una función simple")

funcion_simple();

def funcion_retorno(nombre):
    return nombre;

print(f'Soy una función con retorno: {funcion_retorno("Giovanni")}');


def funcion_varios_parametros(nombre, apellido, fnacimiento):
    return {nombre, apellido, fnacimiento}

print(f'Soy una función de varios parametros: {funcion_varios_parametros("Valentina", "Muñoz", 1992)}');

def funcion_devuelve_diccionario(nombre, apellido, fnacimiento):
    return [nombre, apellido, fnacimiento]

print(f'Function que retorna un diccionario: {funcion_devuelve_diccionario("Dino", "Di Rosa", 1973)}');

def funcion_sin_retorno(profesion):
    print(f'La profesión del paciente es: {profesion}')

funcion_sin_retorno("Médico cirujano")

nombre= "Givoanni fuera de función"
def funcion_ambito_local():
    nombre= "Giovanni dentro de función"
    print(nombre)

funcion_ambito_local();

def funcion_ambito_global():
    print(f'La persona que no coloco la cortina: {nombre}');

funcion_ambito_global();




## EXTRA

"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.

"""

def funcion_imprime(parametro1, parametro2):
    contador= 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(f'{parametro1}-{parametro2}')
        elif numero % 3 == 0:
                print(f'{parametro1}')
        elif numero % 5 == 0:
                print(f'{parametro2}')
        else:
            contador += 1
            print(f'{contador}) {numero}')


funcion_imprime("Fizz", "Buzz")




