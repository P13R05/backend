from Vehiculos import Vehiculo
from Autos import Auto  
from Motos import Moto
from Camiones import Camion
from Concecionario import Concesionaria

def main():
    concesionaria = Concesionaria()

    # Crear instancias de vehículos
    auto1 = Auto("Toyota", "Corolla", 20000, 2020, "sedán" , 4)
    auto2 = Auto("Ford", "Mustang", 35000, 2021, "deportivo ", 2)
    moto1 = Moto("Honda", "CBR500R", 7000, 2019, "deportiva",500)
    moto2 = Moto("Yamaha", "MT-07", 8000,2020, "naked", 700)   
    camion1 = Camion("Ford", "F-150", 30000, 2021, 2)
    camion2 = Camion("Chevrolet", "Silverado", 40000, 2022, 3)
    
# Cambiar el precio usando el setter
    auto1.precio = 21000  # sube de 20000 a 21000
    print("\nDespués de modificar el precio:")
    auto1.mostrar_info()    

# Agregar vehículos a la concesionaria 
    concesionaria.agregar_vehiculo(auto1)
    concesionaria.agregar_vehiculo(moto1) 
    concesionaria.agregar_vehiculo(camion1)
    concesionaria.agregar_vehiculo(auto2)
    concesionaria.agregar_vehiculo(moto2)
    concesionaria.agregar_vehiculo(camion2)
    



# Mostrar catálogo de vehículos
    concesionaria.mostrar_catalogo()
    print("\nBúsqueda de vehículos:")

# Buscar vehículos por marca y modelo   
    concesionaria.buscar_vehiculo("Ford", "Mustang")
    concesionaria.buscar_vehiculo("Honda", "CBR500R")
    concesionaria.buscar_vehiculo("Tesla", "Model S")  # No existe  
if __name__ == "__main__":
    main()      
        