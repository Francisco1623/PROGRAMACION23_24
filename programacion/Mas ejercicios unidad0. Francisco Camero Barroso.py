
#EJERCICIO1
a = int(input("Introduce la altura de la pirámide (metros): "))
l = int(input("Introduce la longitud del lado de la base (metros): "))

area = l*l
vol_pir = (area*a)/3 
print(f"Volumen de la pirámide: {vol_pir} metros cúbicos.")

#EJERCICIO2
metros_cub = 2500
cal_piscinas = vol_pir/metros_cub
print(f"Equivale aproximadamente a {cal_piscinas} piscinas olímpicas.")

#EJERCICIO3
num = int(input("Introduce un numero entero: "))

if num == 0:
    print("El numero es cero: true")
else:
    print("El numero es cero: true")


if num >= 0:
    print("El numero es positivo: true")
else:
    print("El numero es positivo: false")

if num < 100:
    print("El numero es menor que 100: true")
else:
    print("El numero es menor que 100: false")

if num % 2 == 0:
    print("El numero es par: true")
else:
    print("El numero es par: false")

#EJERCICIO4
pelotas = int(input("Introduce las pelotas que quieres: "))
rojo = pelotas/3
azul = pelotas/3
amarillo = pelotas/3

print(f"Si el paquete está compuesto por {pelotas} pelotas: {azul} serán azules, {rojo} serán rojas y {amarillo}serán amarillas")


