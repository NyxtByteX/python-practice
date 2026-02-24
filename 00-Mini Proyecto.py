'''
Crear un pequeño programa que:
1. Muestre información personal
2.Haga cálculos matemáticos
3.Use diferentes tipos de datos
4.Verifique tipos con type()
'''

#A. INFORMACIÓN PERSONAL 
#Crear variables
name =  "Ana"
age = 27
height = 1.63 
ana_vector = 27 + 1.63j

#Imprimir cada variable
print(name)
print(age)
print(height)
print(ana_vector)

#Imprimir el tipo de cada variable
print(type(name))
print(type(age))
print(type(height))
print(type(ana_vector))

#2.OPERACIONES MATEMÁTICAS
#Crear 2 números enteros y operar:
x= 9
y = 2
print(x+y) #suma = 11
print(x-y) #resta = 7
print(x*y) #multiplicación = 18
print(x/y) #división = 4.5
print(x//y) #división entera = 4
print(x**y) #potencia = 81
print(x%y) #modulo = 1

#3.ESTRUCTURA DE DATOS

#Crear una lista con 5 comidas favoritas
print("Mis 5 comidas facoritas son:" ,"Chaufa" , "Pollo a la brasa" , 
      "Arroz con pollo" , "ají de gallina" , "Ceviche")

#Crear un diccionario con nombre, edad, país
#Diccionario = Es una estructura de datos que guarda
#que guarda información en formato -> clave : valor 
#(Es como una ficha o formulario)
mi_info = {
    "nombre" : "Carlos",
    "edad" : "26",
    "país" : "Perú" 
}

print(mi_info)
print(type(mi_info)) #dict

#Crear un set con 3 números decimales
#Es una colección de datos que no tiene orden, no permite
#elementos repetidos, se escribe con llaves {} 
#Diferencia con las listas = El set no tiene orden garantizado 
# y no acepta repetidos
num_dec = {2.9, 2.6, 8.8, 19.8, 2.6}
print(num_dec)
print(type(num_dec))

#Crear tupla con 3 colores
#Tupla = Es una colección de datos que tiene orden, permite 
#repetidos, no se puede modificar, y se escribe en ().
colores = ('azul', 'amarillo', 'negro')
print(colores)
print(type(colores))

#4. DESAFÍOS
#Calcular año de nacimiento con la edad
año_act = 2026
edad_act = 27
año_nac = (año_act-edad_act)
print(año_nac)
