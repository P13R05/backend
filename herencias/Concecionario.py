from Vehiculos import Vehiculo

class Concesionaria:
    def __init__(self):
        self.vehiculos = []  # Lista que almacena todos los vehículos

    # Método para agregar un vehículo a la concesionaria
    def agregar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Vehiculo):
            self.vehiculos.append(vehiculo)
        else:
            print("Solo se pueden agregar objetos de tipo Vehiculo.")

    # Método para mostrar catálogo de vehículos con total
    def mostrar_catalogo(self):
        print("Catálogo de vehículos:\n")
        total = 0
        for vehiculo in self.vehiculos:
            print(vehiculo.descripcion())
            total += vehiculo.get_precio()
        print(f"\n Valor total de la concesionaria: ${total}")
    # Método para buscar vehículos por marca y modelo
    def buscar_vehiculo(self, marca, modelo):
        encontrados = [v for v in self.vehiculos if v.marca == marca and v.modelo == modelo]
        if encontrados:
            for vehiculo in encontrados:
                print(vehiculo.descripcion())
        else:
            print("No se encontraron vehículos con esa marca y modelo.")     