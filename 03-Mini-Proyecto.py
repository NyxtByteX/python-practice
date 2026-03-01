#MINIPROYECTO - "ANALIZADOR INTELIGENTE DE NOMBRE"

print("=====\tANALIZADOR DE NOMBRE\t====")

#Variables
nombre, apellido, edad = "Ana","De la Vega", "26"

#Pedir datos
nombre = input("¿Cuál es tu nombre?: ")
apellido = input("¿Cuál es tu apellido?: ")
edad = input("¿Cuál es tu edad?: ")

#Cantidad de caracteres
car_nom= len(nombre)

#Nombre en reverso
reversed_nombre = nombre[::-1]

#Imprimir valores
print(f"\n\tNombre :{nombre}\n\tApellido :{apellido}\n\tEdad :{edad}")
print("\nLongitud del nombre: ", car_nom) #Cantidad total de caracteres del nombre
print("Nombre en mayúsculas: ",nombre.upper()) #Nombre en mayúsculas
print("Nombre en minúsculas: ",nombre.lower()) #Nombre en minúsculas
print("Nombre bien escrito: ",nombre.capitalize()) #Primera letra del nombre en msc y el resto en min

#Desempaquetado de caracteres

if len(nombre) >= 2:
    primera, *medio, ultima = nombre
    print("Primera letra", primera)
    print("última letra", ultima)
elif len(nombre) == 1:
    print("El nombre solo tiene una letra: ",nombre)
else: 
    print("El nombre está vacío.")

print("Nombre invertido: ", reversed_nombre,) #Nombre invertido
print("Empieza con la letra A: ", nombre.startswith("A")) #Si empieza con una letra específica
print("Cuántas n tiene el nombre: ", nombre.count("n")) #Contar la cantidad del caracter escogido

#SLICING
print("Primeras 3 letras:", nombre[:3])
print("Ultimas 2 letras:", nombre[-2:])
print("Nombre sin primera letra:", nombre[1:])

#Validación de edad
if edad.isnumeric():
    print("Edad válida")
else:
    print("Edad inválida")

