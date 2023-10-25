n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

entra = ""

if (n1 <= 0 and n2 <= 0 and n3 <= 0) or (n1 <= 0 and n2 <= 0 and n3 > 0) or (n1 <= 0 and n2 > 0 and n3 <= 0) or (n1 > 0 and n2 <= 0 and n3 <= 0):
    entra = "NO"
else:
    entra = "SI"

while entra == "SI": 
    if n1 <= n2 <= n3:
        print(f"{n1}, {n2}, {n3}")
    elif n1 <= n3 <= n2:
        print(f"{n1}, {n3}, {n2}")
    elif n2 <= n1 <= n3:
        print(f"{n2}, {n1}, {n3}")
    elif n2 <= n3 <= n1:
        print(f"{n2}, {n3}, {n1}")
    elif n3 <= n1 <= n2:
        print(f"{n3}, {n1}, {n2}")
    else:
        print(f"{n3}, {n2}, {n1}")

    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    n3 = int(input("Introduce el tercer número: "))

print("Más de 2 números son 0 o menor")