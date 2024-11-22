from transporte import Transporte

class Automovil(Transporte):
    __marca= ""
    __modelo= ""
    __cilindrada= ""
    __litros= 0

    def __init__(self, marca, modelo, cilindrada, litros, capacidad, color, velocidad, posicion, consumo, metros):
        self.__marca = marca
        self.__modelo = modelo
        self.__cilindrada = cilindrada
        self.__litros = litros
        self.setCapacidad(capacidad)
        self.setColor(color)
        self.setVelocidad(velocidad)
        self.setPosicion(posicion)
        self.setConsumo(consumo)
        self.setMetros(metros)
   
    
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
    def setMarca(self, marca):
        self.__marca = marca
    def setModelo(self, modelo):
        self.__modelo = modelo
    def setCilindrada(self, cilindrada):
        self.__cilindrada = cilindrada
    
    def cargarCombustible(self, litros):
        return f"Se han cargado {litros}"

        


auto1 = Automovil("Nissan", "Navara", "2.5", "2 tonelada", "plormo", 180, 100, "20 km/l", "50")

print(auto1.avanzar(100))
print(auto1.avanzar(800))


print(auto1.retrocede(200))











