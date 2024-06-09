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

# def funcionSinRetorno():
#     print("Una función sin retorno")

# funcionSinRetorno()


# def funcionRetorno():
#     message = "Un mensaje desde una función con retorno"
#     return message

# funcionRetorno()

# def utilsFuncion():
#     message= "Un mensaje desde otra funcion para ser usada en otra funciones"
#     return message

# def randomFuncion():
#     utilsFuncion()

# randomFuncion()

# global_message= "Este es un mensaje global"

# def funcionParaVariable():
#     print("Global=>", global_message)
#     message_local= "Este es un mensaje local"
#     print("Local=>", message_local)

# funcionParaVariable()

# def funcionArgumentoUno(numero):
#     saldo= numero
#     print("Este es el saldo", saldo)

# funcionArgumentoUno(1492)

# def funcionParametroDos(nombre, numero):
#     print(f"es un print con {nombre}, y el numero {numero}")

# funcionParametroDos("Giovanni", 1987)


#EXTRA 

def contador(message_uno, message_dos):
    contador = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0: 
            print(f"{message_uno} {message_dos}")
        elif number % 3 == 0: #verifica que es multiplo de 3
                print(message_uno)
        elif number % 5 == 0:
                print(message_dos)
        else:
            print(number)
            contador += 1
            
    return contador         
      


message_uno = "fizz"
message_dos = "buzz"
print(f"el número de veces que se ha impreso el número en lugar de los textos: {contador(message_uno , message_dos)}")


    