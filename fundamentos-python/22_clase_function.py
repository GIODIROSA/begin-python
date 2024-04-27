
"""
def acceder():
    contador= 3
    contrasena_validar="ina125"
    
    while contador > 0:
        contrasena_ingresada= input("Ingresar una contraseña para ser adivinada: ")
        if contrasena_ingresada == contrasena_validar:
                print("Felicidades")
                break
        else:
                contador -= 1
                print(f"Fallaste intente de nuevo {contador}")
                if contador == 0:
                    print("error--->")
            
acceder()
"""

def acceder(contador, contrasena_validar):
  
    
    while contador > 0:
        contrasena_ingresada= input("Ingresar una contraseña para ser adivinada: ")
        if contrasena_ingresada == contrasena_validar:
                print("Felicidades")
                break
        else:
                contador -= 1
                print(f"Fallaste intente de nuevo {contador}")
                if contador == 0:
                    print("error--->")
            
acceder(3, "ina125")

