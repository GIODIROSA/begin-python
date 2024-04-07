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