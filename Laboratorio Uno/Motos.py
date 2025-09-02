from Vehiculos import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo,precio, año, clase, cilindrada):
        super().__init__(marca, modelo, precio, año )
        self.clase = clase
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"La moto es  {self.clase} de la marca {self.marca}, modelo {self.modelo},cilindrada {self.cilindrada}, año {self.año}, precio ${self.get_precio()}."