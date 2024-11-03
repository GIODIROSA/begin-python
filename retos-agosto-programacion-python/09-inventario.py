
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

# Agregar productos
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Producto ya existe. Actualizando cantidad. ")
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            print("Producto ha sido agregado al inventario")
            self.productos[producto.id]= producto
# ELiminar productos
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f'Producto ID: {id}, eliminado con existo!')
        else:
            print("Producto no encontrado")

inventario1= Inventario()
producto1= Producto(id=1, nombre="Manzana", precio=0.50, cantidad=100)
producto2= Producto(id=2, nombre="Pera", precio=0.75, cantidad=105)

print(inventario1.productos)
inventario1.agregar_producto(producto1)
inventario1.agregar_producto(producto2)
print(inventario1.productos)

