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

suma = 2 + 3
print("Suma", suma)

resta= 3-6
print("Resta", resta)

division = 2 / 4
print("Dividir", division)

resto = 2 % 180
print("Resto", resto) 

asignacion = "se asigna un valor string"
print("Asignacion", asignacion)

mayor = 6 > 2
print("Mayor que", mayor)

menor= 2 < 6
print("Menor que", menor)

igual = 2 == 2
print("Igualdad", igual)

diferencia = 3 != 5
print("Diferencia", diferencia)

# Pertenencia

lista= ["loquesea", "enmanuel", "pedro", "italia"]

if "loquesea" in lista:
    print("Es cierto")

if "Maria" in lista:
    print("Es falso")
else:
    print("Es verdadero")

# Identidad
# is en python se utiliza para la identidad en memoria de un objeto

a = [1,2,3]
b = a
c = [1,2,3]

print(a == b)
print(a == c)
print(a is b)
print(a is c)


# Iterable

names = ["Maria", "Pedro", "Gustavo", "Francisco"]

for name in names:
    print(name)
    if name == "Pedro":
        print("Lo conseguí")
    else: 
        print("Se lo llevó la vieja")

# Excepciones
"""
    
try:
    resultado = 10 / 0
except ValueError as error:
    print(f"Resultado del error {error}")
else: 
    print("No se puede dividir entre 0")
finally:
    print("Fin del programa")
 """

# Extra

def recorrer_numero():
    for numero in range(10, 56):
        if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
            print(numero)
      

recorrer_numero()
            
# for numero in range(10, 56):
#     if numero % 2 == 0: 
#         if numero != 16:
#             if numero % 3 != 0:
#                 print(numero)
            
        

# Nota repasar mas ejercicio de condicionales.






