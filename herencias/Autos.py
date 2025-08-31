from Vehiculos import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio,año, tipo, ):
        super().__init__(marca, modelo, precio, año, )
        self.tipo = tipo

    def descripcion(self):
        return f"El auto es de la marca {self.marca}, modelo {self.modelo}, año {self.año} y es {self.tipo} precio ${self.get_precio()}."