from Sandwitch import sandwitch
from Venta import ventas
from sandwitch_Carne import sandwithch_Carne
from sandwitch_vegetariano import sandwitch_vegetariano

mi_sandwitch = sandwitch("integral", 1250) 
ventas = ventas()
vegetariano = sandwitch_vegetariano("integral", 1000, "lechuga, tomate, cebolla, pimenton")
carne = sandwithch_Carne("ajo", 1500, "pollo,tocineta,queso,costilla")
carne.set_precio(2000)

ventas.agregar_sandwitch(vegetariano)
ventas.agregar_sandwitch(carne)