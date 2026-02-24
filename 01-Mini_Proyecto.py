'''
MINI PROYECTO: "Ficha de Usuario Inteligente"
Crear un programa que:
1.Pida datos al usuario
2.Convierta tipos correctamente
3.Calcule información
4.Muestre un resumen final
5.Use len(), type(), concatenación y casting
'''

#Mensaje de Bienvenida
print("Bienvenidos al sistema de registro")

#Pedimos datos (nombre,edad,altura,si es estudiante o no)
nombre = input('¿Cuál es tu nombre?: ')
edad_ac = input('¿Cuál es tu edad?:  ')
alt_m = input('¿Cuál es tu altura?:  ')
estudia = input('¿Estudia? (Si/No): ')

#Convertimos tipos
edad_ac = int(edad_ac)
alt_m = float(alt_m)

#Convertimos estudiante a booleano
if estudia.lower() == "Si":
    estudia = True
else:
    estudia = False

#Cálculos
car_nom = len(nombre)
edad_fut = edad_ac + 5
alt_cm = alt_m * 100

#Mostramos resultados
print('----FICHA DE USUARIO-----')
print('Nombre: ',nombre)
print('Caracteres del nombre: ', car_nom)
print('Edad actual: ',edad_ac)
print('Edad en 5 años: ', edad_fut)
print('Altura en metros: ',alt_m)
print('Altura en cm', alt_cm)
print('¿Es estudiante?', estudia)
print('Tipo de Edad:', type(edad_ac))
print('Tipo de Altura:', type(alt_m))
print('Tipo de estudiante:', type(estudia))



