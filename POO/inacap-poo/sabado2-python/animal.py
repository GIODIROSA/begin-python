
from transporte import Transporte

class Animal(Transporte):
    __especie= ""
    __raza = ""
    __energia = 0

    
    
    def __init__(self, especie, raza, capacidad, posicion, energia = 100):
        self.__especie = especie
        self.__raza = raza
        self.__energia = energia
        self.setCapacidad(capacidad)
        self.setPosicion(posicion)
        
        
    def getEspecie(self):
        return self.__especie
    
    def getRaza(self):
        return self.__raza
    
    def getEnergia(self):
        return self.__energia
    
    def getRaza(self):
        return self.__raza
    
    def setEspecie(self, especie):
        self.__especie = especie
    
    def setRaza(self, raza):
        self.__raza = raza
        
    def setEnergia(self, energia):
        self.__energia = energia
    
    
    def comer(self, kilos):
        self.__energia += kilos
        return f"El animal se ha alimentado y ha sumado {kilos} de energia"
    
    def beber(self, litros):
        self.__energia += litros
        return f"Se han sumado {litros} de energia a {self.__energia}"
        
    
    def avanzar(self, posicion= 0):
        self.__posicion += posicion
        return f"avanzando desde {self.__posicion - posicion} a {self.__posicion}: {posicion} "
        
        
        
animal1 = Animal("Equus caballus", "Mustang", 50, 100, 200)

"""    
especie = "Equus caballus"
raza = "Mustang"
capacidad= 50
posicion= 100
energia = 200
        
"""


print(animal1.beber(20))

        






