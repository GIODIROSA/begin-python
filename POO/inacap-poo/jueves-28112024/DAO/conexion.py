import pymysql


class Conexion:
    host = "localhost"
    usuario = "cliente"
    clave = "123456"
    bd = "gestionclientes"
    
    def __init__(self):
        self.db = pymysql.connect(host= self.host, user= self.usuario, password= self.clave, db= self.bd)
        self.cursor = self.db.cursor()
        
    def ejecutarQuery(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def desconectar(self):
        print("Se ha desconectado la base de datos")
        self.db.close()
    
    def commit(self):
        self.db.commit()
    
    def rollback(self):
        self.db.rollback()
        
            
con = Conexion()
cursor = con.ejecutarQuery("SELECT * FROM CLIENTE;")
print(cursor.fetchall())
con.desconectar()


