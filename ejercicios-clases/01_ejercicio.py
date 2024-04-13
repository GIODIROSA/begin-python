
peso_individuo = float(input("Ingrese el peso: "))
altura_individuo= float(input("Ingrese la altura: "))


#print(type(peso_individuo))
#print(type(altura_individuo))


def calcular_IMC(peso_individuo, altura_individuo):
    
    calculo_altura_individuo = (altura_individuo ** 2)
    resultado =  peso_individuo / calculo_altura_individuo
    
    IMC= round(resultado,2)
    if IMC > 0:
        return IMC
    else:
        print("Los valores deben ser números positivos")
        
        
    

print("El calculo de IMC es de: ", calcular_IMC(peso_individuo, altura_individuo))
    


