from Vehiculos import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo,precio, año, capacidad_carga):
        super().__init__(marca, modelo,precio, año)
        self.capacidad_carga = capacidad_carga

    def descripcion(self):
        return f"El camión es de la marca {self.marca}, modelo {self.modelo}, año {self.año} y tiene una capacidad de carga de {self.capacidad_carga} toneladas,  precio ${self.get_precio()}."