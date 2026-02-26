'''
MINI PROYECTO: "EVALUADOR DE ESTUDIANTE"
Crear un programa que pida:
1. Nombre y edad del estudiante
2. Sus 3 notas
3. Calcular el promedio 
4. Determinar si: 
- Está aprobado (promedio >= 11)
- Tiene excelencia (promedio >= 18)
- Está desaprobado
5.Determinar si puede acceder a una beca:
-Promedio mayor o igual a 16
-Edad menos o igual a 20
'''

#Información del alumno
nombre = input('Ingresa tu nombre :')
edad = input('Ingresa tu edad :')
nota_1 = input('Ingresa nota 1 :')
nota_2 = input('Ingresa nota 2 :')
nota_3 = input('Ingresa nota 3 :')

#Convertimos tipos
edad = int(edad)
nota_1 = float(nota_1)
nota_2 = float(nota_2)
nota_3 = float(nota_3)

#Calculos
prom = (nota_1 + nota_2 + nota_3)/3

#Determinar Estado: 
if  prom >= 18:
    estado = ("Excelente")

if prom >= 11 and prom < 18:
    estado = ("Aprobado")

if prom < 11:
    estado = ("Desaprobado")


#Puede acceder a una beca:
beca = "No apto"

if prom >= 16 and edad <= 20:
    beca = ("Apto")

#Imprimir 
print("Estudiante", nombre)
print("Edad", edad)
print("Nota 1", nota_1)
print("Nota 2", nota_2)
print("Nota 3", nota_3)
print("Promedio: ", prom)
print("Estado: ", estado)
print("¿Accede a beca?: ", beca)