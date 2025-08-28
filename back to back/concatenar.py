# True 

# False

# nombre = "Eric"
# saludo = "Bienvenido al curso de prog backend"
# unir = nombre +" "+ saludo

# unir2 = f"Bienvenido {nombre} al curso"

# print(unir2)

# edad = 19
# if edad > 18:
#     print("Puedes pasar")
# else:
#     print("Tas chiquito")
    
# ingresar = input("Quien Eres? ")

# if ingresar.lower() == "balrog":
#     print ("You shall not pass")
# else :
#     print("Puedes pasar")

nota1 = float(input(" Ingresa la Primer nota: "))
nota2 = float(input(" Ingresa la Segunda nota: "))
nota3 = float(input(" Ingresa la Tercera nota: "))

promNotas= (nota1 + nota2 + nota3) / 3
print(promNotas)

if promNotas >= 4:
    print("Aprobaste")
else:
    print("No aprobaste") 