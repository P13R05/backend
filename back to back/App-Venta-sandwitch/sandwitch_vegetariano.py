from Sandwitch import sandwitch

class sandwitch_vegetariano(sandwitch):
    def __init__(self, pan, precio, verduras):
        super().__init__(pan, precio)
        self.verduras = verduras

    def describe(self):
        return f"El sandwitch vegetariano tiene pan {self.pan}, verduras {self.verduras} y cuesta {self.get_precio()} pesos."
     