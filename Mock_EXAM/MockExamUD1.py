"""
#EJERCICIO3
empleados = int(input("Introduce el numero de empleados: "))

ptotal_edad = 0
jtotal_edad = 0
python = 0
java = 0
pmujeres = 0
phombres = 0
jmujeres = 0
jhombres = 0
empleados_nuevo = empleados

while empleados > 0:

    edad = int(input("Introduce tu edad: "))
    if 18<=edad<=65:
        sexo = input("Introduce tu sexo(H/M): ").upper()
        if sexo == "H" or sexo == "M":
            lenguaje = input("Introduce tu lenguaje de programación habitual(python/java): ").upper()
            if lenguaje == "PYTHON" or lenguaje == "JAVA":

                empleados-=1

                if lenguaje == "PYTHON":
                    ptotal_edad += edad
                    python+=1
                    if sexo == "M":
                        pmujeres+=1
                    elif sexo == "H":
                        phombres+=1
                elif lenguaje == "JAVA":
                    jtotal_edad += edad
                    java+=1
                    if sexo == "M":
                        jmujeres+=1
                    elif sexo == "H":
                        jhombres+=1

    
media_python = (python/empleados_nuevo)*100
media_java = (java/empleados_nuevo)*100

pmedia_edad = (ptotal_edad/python)
jmedia_edad = (jtotal_edad/java)


print(f"El {media_python}% de empleados utiliza python, de los que {phombres} son hombres y {pmujeres} son mujeres y su edad media es de {pmedia_edad} años")
print(f"El {media_java}% de empleados utiliza java, de los que {jhombres} son hombres y {jmujeres} son mujeres y su edad media es de {jmedia_edad} años")


"""
"""
#EJERCICIO3
empleados = int(input("Introduce el numero de empleados: "))

ptotal_edad = 0
jtotal_edad = 0
python = 0
java = 0
pmujeres = 0
phombres = 0
jmujeres = 0
jhombres = 0
empleados_nuevo = empleados

for i in range(empleados):

    edad = int(input("Introduce tu edad: "))
    while 18<=edad<=65:
        sexo = input("Introduce tu sexo(H/M): ").upper()
        while sexo == "H" or sexo == "M":
            lenguaje = input("Introduce tu lenguaje de programación habitual(python/java): ").upper()
            while lenguaje == "PYTHON" or lenguaje == "JAVA":

                if lenguaje == "PYTHON":
                    ptotal_edad += edad
                    python+=1
                    if sexo == "M":
                        pmujeres+=1
                    elif sexo == "H":
                        phombres+=1
                elif lenguaje == "JAVA":
                    jtotal_edad += edad
                    java+=1
                    if sexo == "M":
                        jmujeres+=1
                    elif sexo == "H":
                        jhombres+=1

    
media_python = (python/empleados_nuevo)*100
media_java = (java/empleados_nuevo)*100

pmedia_edad = (ptotal_edad/python)
jmedia_edad = (jtotal_edad/java)


print(f"El {media_python}% de empleados utiliza python, de los que {phombres} son hombres y {pmujeres} son mujeres y su edad media es de {pmedia_edad} años")
print(f"El {media_java}% de empleados utiliza java, de los que {jhombres} son hombres y {jmujeres} son mujeres y su edad media es de {jmedia_edad} años")
"""
#EJERCICIO2


opcion = 0

total_alumnos = 0


while opcion != 4:

    print("#######################")
    print("# Bienvenido al IES Jacarandá!!: ")
    print("     1. Alumnos que han entrado: ")
    print("     2. Alumnos que han abandonado el centro: ")
    print("     3. Alumnos en el IES: ")
    print("     4. Salir ")
    print("#######################")

    opcion = int(input("Introduce un número del 1 al 4: "))


    if opcion == 1:

        alumnos_entran = int(input("Introduce los alumnos que entran: "))
        total_alumnos+=alumnos_entran

    elif opcion == 2:
        alumnos_salen = int(input("Introduce los alumnos que salen: "))
        while total_alumnos<alumnos_salen:
            print("No hay suficientes alumnos para que salgan")
            alumnos_salen = int(input("Introduce los alumnos que salen: "))

        total_alumnos-=alumnos_salen


    elif opcion == 3:
        print(f"El total de alumnos que hay en el centro son: {total_alumnos} alumnos")
        
print("Has salido.")