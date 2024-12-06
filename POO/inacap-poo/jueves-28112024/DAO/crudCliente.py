from DTO.cliente import Cliente
from DAO.conexion import Conexion


class CrudCliente:
    cli = []
    
    def mostrar(self):
        con = Conexion()
        cursor= con.ejecutarQuery("Select * from cliente;")
        clientes = cursor.fetchall()
        for cliente in clientes:
            self.cli.append(cliente)
        return self.cli
    
    
    def insertarCliente(self, cliente):
        rut= cliente.getRut()
        nombre= cliente.getNombre()
        apellido = cliente.getApellido()
        direccion = cliente.getDireccion()
        fono = cliente.getFono()
        correo = cliente.getCorreo()
        montoCredito = cliente.getMontoCredito()
        deuda = cliente.getDeuda()
        tipo = cliente.getTipo()
        
        con = Conexion()
        con.ejecutarQuery(f"INSERT INTO cliente into values '{rut}','{nombre}', '{apellido}', '{direccion}', '{fono}', '{correo}', '{montoCredito}', '{deuda}', '{tipo}' ")
        con.commit()
        con.desconectar()