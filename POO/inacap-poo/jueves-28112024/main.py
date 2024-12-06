

from DAO.crudCliente import CrudCliente
from DTO.cliente import Cliente
from DTO.tipo import Tipo


crud = CrudCliente()
print(crud.mostrar())


estandar = Tipo()
Denisse = Cliente(0, estandar, 1000, 10000, 123123, "Denisse", "Quimen", "Paine", 34145253, "denisse@gmail.com")

crud.insertarCliente(Denisse)

