# Vehiculo es la clase base
class Vehiculo:
    def __init__(self, marca, modelo, precio, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.__precio = precio
# Método para describir el vehículo
    def descripcion(self):
        return f"el vehivulo posee {self.marca} {self.modelo} {self.__precio} y fue armado el año ({self.año}), precio ${self.get_precio()}."
    
#getters
    def get_precio(self):
        return self.__precio    
#setters
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")
            
    def mostrar_info(self):
        print(self.descripcion())
            