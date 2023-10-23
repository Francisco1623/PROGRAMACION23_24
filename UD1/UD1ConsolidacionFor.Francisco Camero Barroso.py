#EJERCICIO1
#n  |i  |resultado
#15 |0  |0
#15 |1  |3
#15 |2  |7
#15 |3  |14
#15 |4  |22
#15 |5  |33
#15 |6  |45
#15 |7  |60
#15 |8  |76
#15 |9  |95
#15 |10 |115
#15 |11 |138
#15 |12 |162
#15 |13 |188
#15 |14 |216
#15 |15 |247

#RESULTADO = 247
"""
#EJERCICIO2
num = int(input("Introduce un numero: "))
cadena = ""
for i in range(num):
    cadena+="*"
    print(cadena)

#EJERCICIO3
n = int(input("Introduce un numero: "))
cadena = n*"*"
for i in range(num):
    print(cadena)

#EJERCICIO4
n = int(input("Introduce un numero: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n:
            print(" * ", end="")
        else:
            if j == 1 or j == n:
                print(" * ",end="")
            else:
                print("   ", end="")
    print("")
"""