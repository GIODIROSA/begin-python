from tipo import Tipo


class Cliente:
    __codigo = 0
    __tipo = None #programar
    __montoCredito = 0
    __deuda= 0
    
    def __init__(self, codigo, tipo, montoCredito, deuda):
        self.__codigo= codigo
        self.__tipo= tipo
        self.__montoCredito = montoCredito
        self.__deuda = deuda
        
    def pagar(self,monto):
        pass
    
    def __str__(self):
        return f"Codigo: {self.__codigo} Tipo: {self.__tipo.getCodigo()} -{self.__tipo.getNombre()} "
                
    

Estandar = Tipo(0, "Estandar")
Nicolas = Cliente(1, Estandar, 1000000, 2000000)

print(Nicolas)

