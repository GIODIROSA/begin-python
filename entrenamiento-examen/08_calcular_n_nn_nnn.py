# Ejercicio: Solicitar al usuario un número n y calcular n + nn + nnn

n = input("Escribir el valor de n: ")

nn= int("{}{}".format(n,n))
nnn = int("%s%s%s" % (n,n,n))
n = int(n)

suma = n + nn + nnn

print(suma)