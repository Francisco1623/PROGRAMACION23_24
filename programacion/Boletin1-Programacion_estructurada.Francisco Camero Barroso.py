"""
#EJERCICIO1
mes = int(input("Introduce un numero de mes: "))
if mes < 12:
    print("valor correcto")
#EJERCICIO2
mes = int(input("Introduce un numero de mes: "))
if mes < 12:
    print("valor correcto")
if mes < 6:
    print("el mes es menor que 6")


#EJERCICIO3
numero = int(input("Introduce un numero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par.")



#EJERCICIO4

num1 = int(input("Introduce un numero: "))
if num1 % 2 == 0 and num1 % 3 == 0:
    print("Si, es multiplo de 2 y de 3")

#EJERCICIO5

num1 = int(input("Introduce un numero: "))
if num1 % 2 == 0 and num1 % 3 == 0:
    print("Si, es multiplo de 2 y de 3")
    if num1 % 2 == 0:
        if num1 % 6 == 0:
            print("Múltiplo de 6")
        
        



#EJERCICIO6
num1 = int(input("Introduce un numero: "))
if num1 % 2 == 0 and num1 % 3 == 0:
    print("Si, es multiplo de 2 y de 3")
    if num1 % 2 == 0:
        if num1 % 6 == 0:
            print("Múltiplo de 6")
else:
    print("El numero es impar")

#EJERCICIO7
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if num1 > num2:
    print("El primero mayor que el segundo")
elif num2 > num1:
    print("El segundo mayor que el primero")
else:
    print("Son iguales")

#EJERCICIO8
num1 = int(input("Introduce un numero: "))

if num1 % 2 == 0:
    print(f"El número {num1} es múltiplo de 2")
if num1 % 3 == 0:
    print(f"El número {num1} es múltiplo de 3") 

#EJERCICIO9
edad = int(input("Introduce la edad: "))

if edad < 100:
    if 0 <= edad <= 12:
        print("niño")
    elif 13 <= edad <=17:
        print("adolescente")
    elif 18 <= edad <=29:
        print("joven")
    else:
        print("adulto")
else:
    print("ERROR")

#EJERCICIO10
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))
num3 = int(input("Introduce otro numero: "))
num4 = int(input("Introduce otro numero: "))

media = (num1+num2+num3+num4)/4
print(f"La media es: {media}")

if num1 > media:
    print(f"El {num1} es superior a la media")
if num2 > media:
    print(f"El {num2} es superior a la media")
if num3 > media:
    print(f"El {num3} es superior a la media")
if num4 > media:
    print(f"El {num4} es superior a la media")

    
#EJERCICIO 11
caracter = input("Introduce un caracter: ")

if caracter == "A" or caracter == "a":
    print(f"Es la primera vocal ({caracter})")
elif caracter == "E" or caracter == "e":
    print(f"Es la segunda vocal ({caracter})")
elif caracter == "I" or caracter == "i":
    print(f"Es la tercera vocal ({caracter})")
elif caracter == "O" or caracter == "o":
    print(f"Es la cuarta vocal ({caracter})")
elif caracter == "U" or caracter == "u":
    print(f"Es la quinta vocal ({caracter})")
else:
    print(f"{caracter} no es vocal")

#EJERCICIO12
estado_civil = input("¿Qué estado civil eres?(S-Soltero, C-Casado, V-Viudo y D-Divorciado)")
edad = int(input("Introduce una edad: "))

if estado_civil == "S" or estado_civil == "D" and edad < 35:
    print("12%")
elif edad > 50:
    print("8.5%")
elif estado_civil == "V" or estado_civil == "C" and edad < 35:
    print("11.3%")
else:
    print("10.5%")

#EJERCICIO13
caracter = input("Introduce un caracter: ")
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if caracter == "+":
    print(num1+num2)
elif caracter == "-":
    print(num1-num2)
elif caracter == "/":
    print(num1/num2)
elif caracter == "*":
    print(num1*num2)
else:
    print("ERROR")


#EJERCICIO14
nota_examen = int(input("Introduce tu nota: "))

if 90<=nota_examen<=100:
    print("A")
elif 80<=nota_examen<=89:
    print("B")
elif 70<=nota_examen<=79:
    print("C")
elif 60<=nota_examen<=69:
    print("D")
elif nota_examen < 60:
    print("F")
"""


    
