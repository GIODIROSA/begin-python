nota1= float(input("Ingrese la primera nota: "))
nota2= float(input("Ingrese la segunda nota: "))
nota3= float(input("Ingrese la tercera nota: "))

promedio= round(nota1 + nota2 + nota3) / 3
print(promedio)

if promedio >= 6.0:
    print("Felicidades aprobaste")
elif promedio >= 4.0:
    print("Muy bien, pasaste distinguido")
else:
    print("Se te quedo en la materia amigo")  


print("Final del programa")


#nota:

contador = 1

while contador <= 10:
    print("Iteración", contador)
    contador += 1
    
print("Fin del programa")

#ciclo for

frutas = ["Manzana", "Pera", "Naranja", "Platano"]

for fruta in frutas:
    print("=>",fruta)
    
print("Programa terminado")


ferias = ["Manzana", "Pera", "Naranja", "Platano"]

for fruta in ferias:
    if fruta == "Naranja":
        continue #omitir
    
    print(fruta)



