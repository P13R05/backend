from Vehiculos import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo,precio, año, clase ):
        super().__init__(marca, modelo, precio, año )
        self.clase = clase

    def descripcion(self):
        return f"La moto es  {self.clase} de la marca {self.marca}, modelo {self.modelo}, año {self.año}, precio ${self.get_precio()}."