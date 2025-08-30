from Sandwitch import sandwitch

class ventas:
    def __init__(self):
        self.sandwitches_pedidos = []
    
    def agregar_sandwitch(self, sandwitch):
        print(f"Agregando sandwitch: {sandwitch.descripcion()}, precio ${sandwitch.get_precio()}")
        self.sandwitches_pedidos.append(sandwitch)
        
    def mostrar_ventas (self):
        print("------ Resumen de la Venta ------:")
        total = 0
        for s in self.sandwitches_pedidos:
            print(f" {s.descripcion()} | {s.get_precio()} pesos")
            total += s.get_precio()
        print(f"Total a pagar: ${total} pesos")           