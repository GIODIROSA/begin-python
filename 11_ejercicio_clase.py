
"""
1. Solicite al usuario el ingreso de un número y muestre por pantalla el cálculo de su Factorial paso a paso: """

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Solo se permiten números enteros positivos para calular su factorial.")
else:
    resultado = 1

    for i in range(1, numero + 1):
        print(resultado,'X', i, '=', resultado * i)
        resultado *= i

print(f"El factorial de {numero} es: {resultado}")

