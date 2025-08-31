from Sandwitch import sandwitch

class sandwithch_Carne(sandwitch):
    def __init__(self, pan, precio, tipo_carne):
        super().__init__(pan, precio)
        self.tipo_carne = tipo_carne

    def describe(self):
        return f"El sandwitch de carne tiene pan {self.pan}, carne {self.tipo_carne} y cuesta {self.get_precio()} pesos."