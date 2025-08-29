
# miLista = ["Eric", "Profesor", 39 , 1.80, "curso de prog" ]

# print(miLista[2])

# numeros = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

# print("Lista 1 : ", numeros)

# numeros.append(11)

# numeros.remove(5)

# print("Lista 2 : ", numeros)


# numero1=  float(input ("Ingrese el primer numero: "))
# numero2= float(input ("Ingrese el segundo numero: "))
   
# sumnum = numero1 + numero2
# print("La suma de los numeros es ", sumnum)



# restarnum = numero1 - numero2 
# print("La resta de los numeros es : ", restarnum)

# multiplicarnum = numero1 * numero2 
# print("La multiplicacion es : ", multiplicarnum)
   
# lista_vacia = []
# lista_numeros = [64, 35, 14, 61, 88]
# lista_cadenas = ["Hola", "Mundo", "Python"]
# lista_mixta = [1, "Hola", 3.14, True]

# for i in range(5):
#     print(i)

# frutas = ["manzana", "banana", "cereza"]    

# frutas.append("naranja")    
# print("que es un apend? ", frutas)

# #insert
# frutas.insert(1, "kiwi")
# print("se agrego una : ", frutas)
# #remove
# frutas.remove("banana")
# print("se elimino una : ", frutas)
# #pop
# frutas.pop()
# print("se elimino la ultima : ", frutas)
# #del
# del frutas[0]
# print("se elimino la primera : ", frutas)               
# #clear
# frutas.clear()
# print("se elimino todo : ", frutas)     



# lista_numeros.sort()
# print("lista ordenada : ", lista_numeros)
# lista_numeros.sort(reverse=True)
# print("lista ordenada de mayor a menor : ", lista_numeros)

# #Como buscar los elementos comunes entre dos listas

# lista_A = [1,2,3,4,5,6]
# lista_B = [4,5,6,7,8,9]

# comunes = []
# for elemento in lista_A:
#     if elemento in lista_B:
#         comunes.append(elemento)    
# print("Elementos comunes: ", comunes)
# #metodo 2
# comunes = []
# for i in range(len(lista_A)):
#     for j in range(len(lista_B)):
#         if lista_A[i] == lista_B[j] and lista_A[i] not in comunes:
#             comunes.append(lista_A[i])
# print("Elementos comunes (método 2): ", comunes)    

productos = ["laptop", "teclado", "mouse", "monitor"]
precios = [1200, 250, 80, 300]
existencias = [15,50,30,20]


#ud debe listar los productos por orden y mostrar su precio y existencia
for i in range(len(productos)):
    print(f"Producto: {productos[i]}, Precio: ${precios[i]}, Existencias: {existencias[i]}")  
    total_inventario = 0 
    total_inventario += precios[i] * existencias[i]
    print(f"El total del inventario es: ${total_inventario}")

#ud debe listar los productos por orden alfabetico y mostrar su precio y existencia
# productos_ordenados = sorted(productos)
# for producto in productos_ordenados:
#     indice = productos.index(producto)
#     print(f"Producto: {producto}, Precio: ${precios[indice]}, Existencias: {existencias[indice]}")  
#     total_inventario = 0 
#     total_inventario += precios[indice] * existencias[indice]
#     print(f"El total del inventario es: ${total_inventario}")

#ahora hay que calcular el valor total del inventario
total_inventario_maximo = 0
for i in range(len(productos)):
    total_inventario_maximo += precios[i] * existencias[i]
print(f"El total del inventario maximo es: ${total_inventario_maximo}")