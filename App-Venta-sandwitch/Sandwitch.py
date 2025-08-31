
class sandwitch:
    def __init__(self, pan, precio ):
        self.pan = pan
        self.__precio = precio

    def describe(self):
        return f"El sandwitch tiene pan {self.pan} y cuesta {self.__precio} pesos."

#getters 
    def get_precio(self):
        return self.__precio
   
   #setter
    def set_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")    
            
#metodo que cambia segun el sandwich              
    def descripcion(self):
        return f" Sandwitch con{self.pan}"
            