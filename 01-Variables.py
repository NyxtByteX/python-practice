# Variables

from operator import le

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_into_to_str_variable = str(my_int_variable)
print(my_into_to_str_variable)
print(type(my_into_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, my_into_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable)) #cuenta los caracteres

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, "Mi edad es:", age, "y mi alias es:", alias)

# Inputs
'''
name = input('¿Cuál es tu nombre?: ')
age = input('¿Cuántos años tienes?: ')
print(name)
print(age)
'''

#Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# Forzamos el tipo
addres: Str = "Mi dirección"
addres = True
addres = 5
addres = 1.2
print(type(addres))