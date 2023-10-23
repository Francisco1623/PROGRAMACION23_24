#EJERCICIO1

#total = 64

#EJERCICIO2
#total = 15
"""
#EJERCICIO3
for i in range(10,0,-1):
    print(i)

#EJERCICIO4
num = int(input("Introduce un numero: "))

for i in range(11):
    res = num * i
    print(f"{num} * {i} = {res}")

#EJERCICIO5
for i in range (3, 31, 3):
    print(i)

#EJERCICIO6
n = int(input("Introduce un numero: "))

for i in range(1,n+1):
    print(i)

#EJERCICIO7
for i in range(0,100,7):
    print(i)

#EJERCICIO8
for i in range(10):
    if i % 2 != 0:
        print(i)

#EJERCICIO9
num = int(input("Introduce un numero: "))

fac = 1

for i in range (1,num+1,1):
    fac = fac * i
    
    print(fac)

"""




"""
#EJERCICIO10
num = int(input("Escribe un numero: "))
cont_primos = 0
for i in range(2, num+1):
    for j in range(2, i):
        if i % j == 0:
            print(f"{i} no es primo")
            break

    else:
        print(f"{i} es primo")
        cont_primos += 1

print(f"Entre el 1 y el {num} hay {cont_primos} números primos")

--------------------------------------------

numero = int (input("Introduce un número para ver si es primo: "))
numeroDivisores = 0
for divisor in range(2,numero, 1) :
    if numero % divisor == 0 :
        numeroDivisores = numeroDivisores+1
if numeroDivisores > 0 :
    print(numero, " NO es PRIMO")
else:
    print(numero, " es PRIMO")
"""















    


        
    












