
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.nombre} (ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad})'


class Inventario:
    def __init__(self):
        self.productos= {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Producto ya existe. Actualizando cantidad. ")
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id]= producto

inventario1= Inventario()
producto1= Producto(id=1, nombre="Manzana", precio=0.50, cantidad=100)
print(inventario1.productos)
inventario1.agregar_producto(producto1)
print(inventario1.productos)

