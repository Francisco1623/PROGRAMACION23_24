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