### Strings ### 

#Creamos 2 variables tipo string
my_string = 'Mi String'
my_other_string = 'Mi otro String'

#len() devuelve la cantidad de caracteres
print(len(my_string))
print(len(my_other_string))

#Concatenación: unimos 2 strings usando +
#"" -> Se agrego un espacio manualmente
print(my_string + " " + my_other_string)

# \n es una secuencia de escape que genera un salto de línea
my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

# \t es una secuencia de escape que genera una tabulación (TAB)
my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

# \\ permite mostrar la barra invertida literal
# Aquí NO se ejecuta \t ni \n porque están escapados
# Se imprimirán como texto normal: \t y \n
my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)


#FORMATEO
name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname,age)) # {} son marcadores de posición // .format() reemplaza esos {} en orden
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # %s --> string // %d --> número entero  (digit)  
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Concatenación manual  
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #La f delante del string activa el formato dinámico // dentro de {} puedes poner variables

#DESEMPAQUETADO DE CARACTERES (asignación múltiple de elementos iterables)
languaje = "Python" # Un string es iterable, por eso podemos separar cada letra en variables
a, b, c, d, e, f = languaje # Cada variable recibe un carácter en orden
print(a) # Imprime la primera letra: 'P'
print(e) # Imprime la primera letra: 'O'
#OJO: El número de variables debe coincidir con el número de caracteres, si no lanzará un ValueError

#DIVISIÓN // SLICING (Corte de strings)
# Sintaxis: string[inicio:fin] - [Incluye el inicio : No incluye el fin]
languaje_slice = languaje[1:3] # Extrae desde la posición 1 hasta antes de la 3 → "yt"
print(languaje_slice)

languaje_slice = languaje[1:] # Desde la posición 1 hasta el final → "ython"
print(languaje_slice)

languaje_slice = languaje[-2] # Índice negativo: cuenta desde el final//-2 es la segunda letra desde el final → "o"
print(languaje_slice)

languaje_slice = languaje[1:2:4] # Extrae desde la posición 1 hasta antes de la 2, como el rango solo contiene una letra, el paso 4 no cambia el resultado. Resultado: "y"
print(languaje_slice)


#REVERSE (Invertir string)
# Sintaxis: string[inicio:fin:paso]
# No especificamos inicio ni fin → toma todo el string
# Paso = -1 → recorre el string hacia atrás
reversed_languaje = languaje[::-1]
print(reversed_languaje) # "nohtyP"