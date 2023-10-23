#EJERCICIO1
#El resultado de producto es depende de el numero que le pongamos al principio, cuando nos piden un numero.
#Lo que hace este código es pedir un numero positivo, iniciamos variables "producto" e "i", hacemos un bucle 
#que si i es menos o igual al numero que pusimos entra al bucle en el que consiste en que "producto" se multiplica por "i", 
#el resultado se le asigna a "producto" y le suma a la "i" 1 para que cuando sea mayor "i" al numero que pusimos anteriormante salga del bucle 
#y nos muestre el print.

#i  |producto
#1  |1
#2  |2
#3  |6
#4  |24
#5  |120
#... así hasta que la i sea mayor que el numero que pusimos.

#EJERCICIO2

#N  |suma   |i
#6  |1      |1
#6  |3      |2
#6  |3      |3
#6  |7      |4
#6  |7      |5
#6  |13     |6

#suma = 13
"""
#EJERCICIO3
limite = 10

while 1 <= limite:
    print(limite)
    limite-=1
    

#EJERCICIO4
num = int(input("Introduce un numero: "))
suma = 0
while num != 0:
    suma+=num
    num = int(input("Introduce un numero: "))
print(suma)

#EJERCICIO5

num = int(input("Introduce un numero: "))
cont = 0
while cont <= 10:
    res = cont * num
    print(f"{num}x{cont} = {res}")
    cont+=1

#EJERCICIO6
import random


num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

while num1 != 0 or num2 != 0:
    print(num1+num2)
    num1 = int(input("Introduce un numero: "))
    num2 = int(input("Introduce otro numero: "))

#EJERCICIO7
import random


num = int(input("Introduce un numero: "))
num_random = random.randint(1,10)
intentos = 1
#print(num_random)
while num != num_random:
    if num < num_random:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")

    intentos+=1
    num = int(input("Introduce un numero: "))
print(f"El número de intentos es: {intentos}")



#EJERCICIO8
avance = 3
while avance <= 30:
    print(avance)
    avance+=3

#EJERCICIO9
password = input("Introduce una contraseña: ")

while password != "1234":
    password = input("Introduce una contraseña: ")

print("Bienvenido")

#EJERCICIO10
import random


num_random1 = random.randint(0,10)
num_random2 = random.randint(0,10)

suma = int(input("¿Cuál es la suma?: "))
suma_random = num_random1+num_random2
#print(suma_random)

while suma != suma_random:
    suma = int(input("¿Cuál es la suma?: "))
"""




    
    
    
