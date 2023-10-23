import random


lista = ["Pepe", True, 3, "Juan", False, 7, "Galindo", True, 11]
lista2 = []
"""
#EJERCICIO 2 EXAMEN CON LISTAS
num = int(input("Introduce un numero: "))
listanum = []
cont_des = 0
cont_asc = 0
cont_igual = 0

while num != 0:

    listanum.append(num)

    for i in range(len(listanum)-1):
        
        if num < listanum[i]:
            cont_asc+=1
            
        if cont_asc > 1:
            
            ascendente = "NO es ascendente"
        else:
            ascendente = "SI es ascendente"

        if num > listanum[i]:
            cont_des+=1
            
        if cont_des < 1:
            
            descendente = "SI es descendente"
        else:
            descendente = "NO es descendente"

        if num == listanum[i]:
            cont_igual+=1

        if cont_igual >= 1:
            repetidos = "SI hay repetidos"
        else:
            repetidos = "NO hay repetidos"

        if (ascendente == "NO es ascendente" and descendente == "NO es descendente"):
            ordenado = "NO está ordenado"
            
        else:
            ordenado = "SI está ordenado"
            

          


    num = int(input("Introduce un numero: "))


    
print(ascendente)
print(descendente)
print(repetidos)
print(ordenado)




elemento = input("Introduce un elemento: ")


while elemento != "11":



    lista2.insert(0, elemento)
    elemento = input("Introduce un elemento: ")



print(lista2)



elemento = input("Introduce un elemento: ")


while elemento != "11":


    lista2.append(elemento)
    elemento = input("Introduce un elemento: ")



print(lista2)

edades = [2, 3, 4, 5]


i=0
while i < len(edades):
    print(edades[i])  
    i+=1     


#EJERCICIO1
print(lista[:])#Devuelve la lista entera
print(lista[0:len(lista)])#Devuelve los valores de la lista desde la posición 0 hasta el tamaño de la lista.
print(lista[-len(lista):])#Devuelve los valores de la lista desde la posición 0 hasta el tamaño de la lista.
print(lista[:len(lista)])#Devuelve los valores de la lista desde la posición 0 hasta el tamaño de la lista.
print(lista[len(lista)-1])#Devuelve el último valor de la lista. lista[0:9-1] 
print(lista[-1])#Devuelve el último valor de la lista.

#EJERCICIO2
#Muestra el valor del elemento 6 de un array f.
f = [2, 3, 4, 5, 6, 7, 8]
print(f[6])

#Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
f = []
#con while
cont = 0
while cont < 5:
    f.append(8)
    cont+=1
print(f)
#con for
for i in range(5):
    f.append(8)
print(f)

a = ["A", "B", "C"]
b = [1, 2, 3, 4, 5]
b.extend(a)
print(b)

#Total de los 10 elementos de punto-flotante de un array c.
c = [1,2,3,4,5,6,7,8,9,10]
total = 0
for i in c:
    total+=i
print(total)

#Copia los 11 elementos de un array a en la primera porción de un array b, el
#cual contiene 34 elementos.

a = [1,2,3,4,5,6,7,8,9,10,11]
b = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]

b = a+b

print(b)

#Calcula y muestra el valor mayor y menor contenidos en un array w de 99
#elementos de punto-flotante

w = []
for i in range(1,100):
    w.insert(i,i)

print(w)
max_valor = 0
min_valor = 1

for i in range(len(w)-1):
    if i >= max_valor:
        max_valor=i
    if i <= min_valor:
        min_valor=i

print(min_valor)
print(max_valor)

#EJERCICIO3

#con reverse
inverso = []
cont = 0

while cont < 10:
    num1 = int(input("iNTRODUCE UN NUMERO: "))
    cont+=1
    inverso.append(num1)
inverso.reverse()
print(inverso)

#sin reverse
inverso = []
cont_num = 0

while cont_num < 10:
    num1 = int(input("iNTRODUCE UN NUMERO: "))
    cont_num+=1
    inverso.append(num1)

cont = (len(inverso)-1)

while cont >= 0:
    print(inverso[cont])
    cont-=1

    
#EJERCICIO4

numbers = []
squares = []
cubes = []
cont_num = 0

while cont_num < 20:
    num1 = random.randint(0,100)
    cont_num+=1
    numbers.append(num1)

for i in numbers:
    squares.append(i**2)

for i in numbers:
    cubes.append(i**3)

numbers.sort()
squares.sort()
cubes.sort()
print(numbers)
print(squares)
print(cubes) 


#EJERCICIO5


cont_num = 0
w = []
for i in range(1,10):
    num1 = int(input("iNTRODUCE UN NUMERO: "))

    w.append(num1)


max_valor = ""
min_valor = ""

w.sort()
w.insert(0,"min_valor = ")
w.insert(-1,"max_valor = ")
print(w)
"""





    





   









   





