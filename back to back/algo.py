#tres clases y 2 metods (ejemploS de POO) 
class Persona:
     def __init__(self, nombre, edad, rut):
         self.nombre = nombre
         self.edad = edad
         self.id = rut #atributo unico

     def saludar(self):
         print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
         
class Animal:
    def __init__(self, especie, nombre, edad):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self, sonido):
        print(f"{self.nombre} dice: {sonido}")         

class Vehiculo:
    def __init__(self, marca, modelo, ):
        self.marca = marca
        self.modelo = modelo
        

    def descripcion(self):
        print(f"Vehículo: {self.marca} {self.modelo}, ")        
        
        
        
        
mi_persona = Persona("Juan", 30, "12345678-9")
mi_persona.saludar()            