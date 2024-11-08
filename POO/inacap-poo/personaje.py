
 
class Personaje:
    __nombre= ""
    __nivel= 0
    __salud = 0
    __energia = 0
        
    def __init__(self, nombre, nivel, salud, energia):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__salud= salud
        self.__energia= energia
        
    def getNombre(self):
        return self.__nombre
    
    def getNivel(self):
        return self.__nivel
    
    def getSalud(self):
        return self.__salud
    
    def getEnergia(self):
        return self.__energia
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
