
from transporte import Transporte

class Animal(Transporte):
    __especie= ""
    __raza = ""
    __energia = 0
    
    
    def __init__(self, especie, raza, capacidad, color, energia = 100):
        self.__especie = especie
        self.__raza = raza
        self.__energia = energia
        self.getCapacidad(capacidad)
        self.getColor(color)
        self.get
        
        
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
    
    
    def comer(self, energia):
        self.__energia = energia
        return f"El animal se ha alimentado y ha sumado {energia} de energia"
    
    def beber(self, ):
        pass
    
    def avanzar(self, metros):
        pass
        
        
        
        
        






