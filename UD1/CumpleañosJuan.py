anio = int(input("Introduce el año: "))
puzzle = 1
total_p = 1
dinero = 20
total_d = 0


for i in range(2,anio):

    if anio % 2 == 0:
        dinero+=15
    else:
        puzzle*=2
    total_d+=dinero
    total_p+=puzzle
print(total_d)
print(total_p)