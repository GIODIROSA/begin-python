
"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

## Suma
suma = 2 + 2
print("suma=>", suma)

## resta
resta= 2-2
print("resta=>", resta)

## Multiplicar
multiplicar= 3*3
print("Multiplicar", multiplicar)

## Dividir
dividir= 2//2
print ("division", dividir)

## modulo
modulo= 3 % 3
print("Modulo", modulo)

## condicional
loquesea= "loquesea"
if loquesea == "loquesea":
    print("entra al if")
else:
    print("no entro al if")

numero_edad= 18
if numero_edad < 18:
    print("No eres mayor de edad")
else:
    print("Eres mayor de edad")

## Asignacion
asignacion = "Se le asigna un valor"
print("asignacion", asignacion)

## diferente
numero1= 34
numero2= 56

valor = numero1 == numero2
print("valor es:", valor)

valor2 = numero1 != numero2
print("valor es:", valor2)

mayor = 6 > 2
print("mayor", mayor)

menor = 3 < 5
print("menor", menor)

iguales = 2 == 2
print("igual", iguales)

#Pertenencia

lista_nombre= ["Giovanni", "Maria", "Carmen"]

if "Maria" in lista_nombre:
    print("Es cierto")
else:
    print("es falso")

if "Pedro" in lista_nombre:
    print("pedro esta en la lista")
else:
    print("pedro esta fuera de la lista")

# Identidad
# is en python se utiliza para la identidad en memoria de un objeto

a = [1,2,3]
b = a
c = [1,2,3]

print(a == b)
print(a == c)
print(a is b)
print(a is c)


## EXTRA
def recorrer_numero():
    for numero in range(10,56):
        if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
            print("=>", numero)

recorrer_numero();

