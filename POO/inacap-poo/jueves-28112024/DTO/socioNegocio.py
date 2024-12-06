

class SocioNegocio:
    __run = ""
    __nombre = ""
    __apellido = ""
    __direccion = ""
    __fono = 0
    __correo = ""
    
    def getRun(self):
        return self.__run
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDireccion(self):
        return self.__direccion
    
    def getFono(self):
        return self.__fono
    
    def getCorreo(self):
        return self.__correo
    
    def setRun(self, run):
        self.__run= run
        
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setApellido(self, apellido):
        self.__apellido = apellido
    
    def setDireccion(self, direccion):
        self.__direccion = direccion
        
    def setFono(self, fono):
        self.__fono = fono
    
    def setCorreo(self, correo):
        self.__correo = correo
        


