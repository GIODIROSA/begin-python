class Transporte:
    __capacidad= ""
    __color = "blanco"
    __velocidad = 0 
    __posicion = 0
    __consumo = ""
    __metros = ""
  
    
        
    def getCapacidad(self):
        return self.__capacidad
    
    def getColor(self):
        return self.__color
    
    def getVelocidad(self):
        return self.__velocidad
    
    def getConsumo(self):
        return self.__consumo
    
    def getMetros(self):
        return self.__metros
    
    
    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad
        
    def setColor(self, color):
        self.__color = color
    
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad
        
    def setPosicion(self, posicion):
        self.__posicion = posicion
        
    def setConsumo(self, consumo):
        self._consumo = consumo
        
    def setMetros(self, metros):
        self.__metros = metros
        
        
    def avanzar(self, metros= 0):
        self.__posicion += metros
        return f"avanzando desde {self.__posicion - metros} a {self.__posicion}: {metros} metros"
        
        
    def retrocede(self, metros= 0):
        self.__posicion -= metros
        return f"Retroce desde {self.__posicion + metros} a {self.__posicion}: {metros} metros"
    

    
    
    
