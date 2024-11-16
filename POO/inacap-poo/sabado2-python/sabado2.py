class Automovil:
    __marca= ""
    __modelo= ""
    __cilindrada= ""
    __posicion= 0
    def __init__(self, marca, modelo, cilindrada, posicion= 0):
        self.__marca = marca
        self.__modelo = modelo
        self.__cilindrada = cilindrada
        self.__posicion = posicion
    
    def __del__(self):
        print(f"Se ha eliminado el automovil {self.__marca} - {self.__modelo} - {self.__cilindrada}")
        
    def __str__(self) -> str:
        return f"Automovil {self.__marca} {self.__modelo} {self.__cilindrada}"
    
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getCilindrada(self):
        return self.__cilindrada
    def getPosicion(self):
        return self.__posicion
    def setMarca(self, marca):
        self.__marca = marca
    def setModelo(self, modelo):
        self.__modelo = modelo
    def setCilindrada(self, cilindrada):
        self.__cilindrada = cilindrada
    def setPosicion(self, posicion):
        self.__posicion = posicion
    def mostrarPosicion(self):
        return self.__posicion
        
    def avanzar(self, metros= 0):
        self.__posicion += metros
        return f"avanzando desde {self.__posicion - metros} a {self.__posicion}: {metros} metros"
        
        
    def retrocede(self, metros= 0):
        self.__posicion -= metros
        return f"Retroce desde {self.__posicion + metros} a {self.__posicion}: {metros} metros"
        
        




auto1 = Automovil("Nissan", "Navara", "2.5")

print(auto1.avanzar(100))
print(auto1.avanzar(800))


print(auto1.retrocede(200))










