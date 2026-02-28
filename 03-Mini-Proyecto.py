#MINIPROYECTO - "ANALIZADOR INTELIGENTE DE NOMBRE"

#Variables
nombre, apellido, edad = "Ana","De la Vega", "26"
car_nom= len(nombre)

#Pedir datos
nombre = input("¿Cuál es tu nombre?: ")
apellido = input("¿Cuál es tu apellido?: ")
edad = input("¿Cuál es tu edad?: ")

nombre = "Anita"
a,b,c,d,e = nombre

reversed_nombre = nombre[::-1]

#Imprimir valores
print("=====\tANALIZADOR DE NOMBRE\t====")
print(f"\n\tNombre :{nombre}\n\tApellido :{apellido}\n\tEdad :{edad}")
print("\nLongitud del nombre: ", car_nom) #Cantidad total de caracteres del nombre
print("Nombre en mayúsculas: ",nombre.upper()) #Nombre en mayúsculas
print("Nombre en minúsculas: ",nombre.lower()) #Nombre en minúsculas
print("Nombre bien escrito: ",nombre.capitalize()) #Primera letra del nombre en msc y el resto en min
print("Primera letra: ",(a)) #Primera letra del nombre
print("Última letra: ",(e)) #última letra del nombre
print("Nombre invertido: ", reversed_nombre,) #Nombre invertido
print("Empieza con la letra A: ", nombre.startswith("A")) #Si empieza con una letra específica
print("Cuántas n tiene el nombre: ", nombre.count("n"))