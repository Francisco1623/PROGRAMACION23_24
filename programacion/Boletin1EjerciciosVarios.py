#EJERCICIO1
#sumaIt|    sumaTotal|    i|  j|
#     0|            0|    
#     13|          13|    1|  3|
#     12|          25|    1|  2|
#     11|          36|    1|  1|
#     23|          59|    2|  3|
#     22|          81|    2|  2|
#     21|         102|    2|  1|
#     33|         135|    3|  3|
#     32|         167|    3|  2|
#     31|         198|    3|  1|

#sumaTotal = 198
"""
#EJERCICIO2
num = int(input("Introduce un numero: "))

while num >= 0:
    print(f"El numero {num} elevado 2 es: {num**2}")
    num = int(input("Introduce otro numero: "))

    
#EJERCICIO3
num = int(input("Introduce un numero del 1 al 7: "))
suma = 0
while num > 7:
    num = int(input("Introduce un numero del 1 al 7: "))

for i in range(num,7+1):
    suma+=i
    print(i)
print(f"La suma de los números anteriores hasta llegar al 7 es: {suma}")

#EJERCICIO4
al1 = float(input("Introduce la altura del primer alumno: "))
al2 = float(input("Introduce la altura del segundo alumno: "))
al3 = float(input("Introduce la altura del tercero alumno: "))
al4 = float(input("Introduce la altura del cuarto alumno: "))

edad1 = int(input("Introduce la edad del primer alumno: "))
edad2 = int(input("Introduce la edad del segundo alumno: "))
edad3 = int(input("Introduce la edad del tercero alumno: "))
edad4 = int(input("Introduce la edad del cuarto alumno: "))

print("Estos son los que tienen más de 18: ")
if edad1 >= 18:
    print(edad1)
if edad2 >= 18:
    print(edad2)
if edad3 >= 18:
    print(edad3)
if edad4 >= 18:
    print(edad4)

media_al = (al1 + al2 + al3 + al4)/4
print(f"Estos son los que miden menos de la media ({media_al}) de altura: ")

if al1 < media_al:
    print(al1)
if al2 < media_al:
    print(al2)
if al3 < media_al:
    print(al3)
if al4 < media_al:
    print(al4)

#EJERCICIO5
num = int(input("Introduce un numero: "))
num_ele = int(input("Introduce la elevación de el número anterior: "))
total = 1
for i in range(1,num_ele+1):
    total*=num

print(f"{num} elevado entre {num_ele} es: {total} ")

#EJERCICIO6

usuario = input("Introduce un nombre: ")
clave_login = input("Introduce la clave: ")
usuario_login = input("Introduce el usuario: ")

while usuario != usuario_login:
    usuario_login = input("Introduce el usuario: ")

clave = input("Introduce la clave: ")
while clave!=clave_login:
    clave = input("Introduce la clave: ")

print("Logado correctamente.")

#EJERCICIO7
print("TABLAS DE MULTIPLICAR")
for i in range(1,10+1):
    print(f"TABLA DEL {i}")
    print("-----------------------------------")

    for j in range(0,10+1):
        print(f"{i}*{j} = {i*j}")
    print("-----------------------------------")


#EJERCICIO8
precio = float(input("Introduce el precio: "))
suma = 0
while precio > 0:
    suma+=precio
    precio = float(input("Introduce el precio: "))
print(f"El precio total de los productos es: {suma}€")
"""


#EJERCICIO9
precio = float(input("Introduce el precio: "))
suma = 0
while precio > 0:
    suma+=precio
    precio = float(input("Introduce el precio: "))
print(f"El precio total de los productos es: {suma}€")











