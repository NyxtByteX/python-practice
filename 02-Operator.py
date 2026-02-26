### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hola " + "Python " + " ¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola" * int(my_float))

### Operadores Comparativos ###
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#Ordenación alfabética
# Python compara texto letra por letra usando el valor Unicode
# Es decir, realmente compara números internos de cada carácter
print("Hola" >  "Python") # Compara la primera letra: "H"(72)>"P" (80) - False
print("Hola" <  "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores Lógicos ###
print(3 > 4 and "Hola" > "Python") # false and false --> false
print(3 > 4 or "Hola" > "Python") # false or false --> false
print(3 < 4 and "Hola" < "Python") # true and true --> true
print(3 < 4 or "Hola" > "Python") #true or false --> true
print(3 < 4 or ("Hola" > "Python" and 4 ==4 )) # true or (false and true) --> true or false --> true
print(not(3 > 4)) # not(false) -> true