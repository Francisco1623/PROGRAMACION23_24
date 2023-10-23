#EJERCICIO1
numero1 = 12
numero2 = 3

print(numero1*numero2)

#EJERCICIO2
print(numero1%numero2)

#EJERCICIO3

print(float(numero1)+float(numero2))/2

#EJERCICIO4
longitud = 3
milla = 1609

print(milla * longitud)

#EJERCICIO5
c = int(input("Introduzca una temperatura: "))
gradosF = 9*c/5+32
print(gradosF)

#EJERCICIO6
nota1 = float(input("Introduzca una nota: "))
nota2 = float(input("Introduzca otra nota: "))
nota3 = float(input("Introduzca otra nota: "))
nota4 = float(input("Introduzca otra nota: "))

media = (nota1+nota2+nota3+nota4)/4
print(media)

#EJERCICIO7
b = int(input("Introduzca la base: "))
a = int(input("Introduzca la altura: "))

area = b*a/2
print(area)

#EJERCICIO8
h = int(input("Introduzca hora: "))
m = int(input("Introduzca minuto: "))
s = int(input("Introduzca segundo: "))

m = m + (s / 60)
s = s % 60

h = h + (m / 60)
m = m % 60

h = h % 24

print(f"Los valores introducidos dan un resultado de: {h} horas, {m} minutos, {s} segundos")