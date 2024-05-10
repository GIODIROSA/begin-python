class Auto:
    def __init__(self, nombre, modelo, agnio):
        self.nombre = nombre
        self.modelo = modelo
        self.agnio = agnio

    def mostrar_informacion(self):
        print(f"El auto {self.nombre}, modelo: {self.modelo}, año: {self.agnio}")

    def actualizar_agnio_auto(self, nuevo_agnio):
        self.agnio = nuevo_agnio
        print(f"Se ha actualizado el año {self.agnio} del auto")


# Herencia

class Auto_electrico(Auto):
    def __init__(self, nombre, modelo, agnio, bateria_kmh):
        super().__init__(nombre, modelo, agnio)
        self.bateria_kmh = bateria_kmh
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"La bateria es: {self.bateria_kmh}")



mi_auto = Auto("Ford", "EcoSport", 2022)
mi_auto.mostrar_informacion()
mi_auto.actualizar_agnio_auto(2023)
mi_auto_electrico = Auto_electrico("Tesla", "Renacer", 2020, "300GHZ")
mi_auto_electrico.mostrar_informacion()

