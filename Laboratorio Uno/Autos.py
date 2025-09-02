from Vehiculos import Vehiculo

# Auto hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio,año, tipo, puertas ):
        super().__init__(marca, modelo, precio, año, )
        self.tipo = tipo
        self.puertas = puertas

# Método para describir el auto
    def descripcion(self):
        return f"El auto es de la marca {self.marca}, modelo {self.modelo}, año {self.año} y es {self.tipo} con {self.puertas} precio ${self.get_precio()}."