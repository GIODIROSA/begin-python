from tipo import Tipo
from socioNegocio import SocioNegocio


class Cliente(SocioNegocio):
    __codigo = 0
    __tipo = None #programar
    __montoCredito = 0
    __deuda= 0
    
    def __init__(self, codigo, tipo, montoCredito, deuda, run, nombre, apellido, direccion, fono, correo):
        self.__codigo= codigo
        self.__tipo= tipo
        self.__montoCredito = montoCredito
        self.__deuda = deuda
        self.setRun(run)
        self.setNombre(nombre)
        self.setApellido(apellido)
        self.setDireccion(direccion)
        self.setFono(fono)
        self.setCorreo(correo)
        
    def pagar(self,montoCredito):
        pass
    
    def __str__(self):
        return f"Nombre: {self.getNombre()} - Codigo: {self.__codigo} Tipo: {self.__tipo.getCodigo()} - {self.__tipo.getNombre()}"
                
    

Estandar = Tipo(0, "Estandar")
Nicolas = Cliente(1, Estandar, 1000000, 2000000, "26240354-8","Nicolas", "Vasquez", "Inacap", 123456, "nicolas@inacap.cl")

print(Nicolas)

