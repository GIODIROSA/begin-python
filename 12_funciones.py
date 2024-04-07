def Saludar(nombre, apellido):
    print("-" * 20)
    print("Buenas tardes", nombre, apellido)
    print("-" * 20)

nombre= input("Ingresa tu nombre: ")
apellido= input("Ingresa tu apellido: ")

Saludar(nombre, apellido)


def Pagar(producto, precio, formaPago="Efectivo", cantidad=1):
    total= int(precio) * int(cantidad)
    print(producto, "...$", precio, "x", cantidad, "= $", total)
    print("Forma de pago: ", formaPago)


Pagar(producto="coca-cola 3 lts", precio=2300,cantidad=5)

# Function declaración de retorno


def CalcularPrecio(precio, formaPago="Efectivo", cantidad=1):
    if precio > 0 and cantidad >= 1:
        total = int(precio) * int(cantidad)
              
        if formaPago.lower() == "credito":
            print("está entrando")
            descuento= total * 0.1
        else:
            descuento = 0
        totalPagar = total - descuento

        # return print("Total a pagar: ", totalPagar)
        return  [total, descuento, totalPagar]
        
    else: 
        print(f"El precio: {precio} debe ser mayor a 0 y las cantidad: {cantidad} debe ser mayor a 1 ")



pagar = CalcularPrecio(precio=3500, formaPago="CREDITO", cantidad= 2)

print("Total sin descuento: $", pagar[0], "-", pagar[1], "(Descuento) = $", pagar[2])

# Recursividad 
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


print(fibonacci_recursivo(7))

# n1= 0
# n2= 1

# acumulador= n1 + n2 
# n2 = acumulador + n1

# 0+1=1+1=2+1=3+2=5+3=8+5


n1= 0
n2= 1 

for i in range(1, 50+1):
  
    fib= n1 + n2 
    print("=>", fib)
    n1 = n2
    n2 = fib
    # 0+1=1+1=2+1=3+2=5+3=8+5


