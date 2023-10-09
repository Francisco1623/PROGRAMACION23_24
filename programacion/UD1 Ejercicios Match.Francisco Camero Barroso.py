"""
#EJERCICIO1
dia = input("Introduce una cadena: ")
dia = dia.upper()

if dia == "SABADO" or dia == "DOMINGO":
    print("Día de estudio y reflexión")
elif dia == "LUNES" or dia == "MARTES" or dia == "MIERCOLES" or dia == "JUEVES" or dia == "VIERNES":
    print("================================")
    print(dia)
    print("================================")

    if dia == "LUNES":
        print("8-9 FOL")
        print("9-10 ENT")
        print("10-11 PROG")
        print("11-11:30 RECREO")
        print("11:30-12:30 PROG")
        print("12:30-13:30 BBD")
        print("13:30-14:30 BBD")
        print("================================")


    elif dia == "MARTES":
        print("8-9 FOL")
        print("9-10 FOL")
        print("10-11 SIST")
        print("11-11:30 RECREO")
        print("11:30-12:30 SIST")
        print("12:30-13:30 LENG")
        print("13:30-14:30 LENG")
        print("================================")

    elif dia == "MIERCOLES":
        print("8-9 ENT")
        print("9-10 ENT")
        print("10-11 PROG")
        print("11-11:30 RECREO")
        print("11:30-12:30 PROG")
        print("12:30-13:30 BBD")
        print("13:30-14:30 BBD")
        print("================================")

    elif dia == "JUEVES":
        print("8-9 PROG")
        print("9-10 PROG")
        print("10-11 BBD")
        print("11-11:30 RECREO")
        print("11:30-12:30 BBD")
        print("12:30-13:30 SIST")
        print("13:30-14:30 SIST")
        print("================================")

    elif dia == "VIERNES":
        print("8-9 SIST")
        print("9-10 SIST")
        print("10-11 LENG")
        print("11-11:30 RECREO")
        print("11:30-12:30 LENG")
        print("12:30-13:30 PROG")
        print("13:30-14:30 PROG")  
        print("================================")
  
else:
    print("VALOR INCORRECTO")


#CON MATCH

match dia:
    case "LUNES":
        print("================================")
        print(dia)
        print("================================")

        print("8-9 FOL")
        print("9-10 ENT")
        print("10-11 PROG")
        print("11-11:30 RECREO")
        print("11:30-12:30 PROG")
        print("12:30-13:30 BBD")
        print("13:30-14:30 BBD")
        print("================================")
    case "MARTES":
        print("8-9 FOL")
        print("9-10 FOL")
        print("10-11 SIST")
        print("11-11:30 RECREO")
        print("11:30-12:30 SIST")
        print("12:30-13:30 LENG")
        print("13:30-14:30 LENG")
        print("================================")
    case "MIERCOLES":
        print("8-9 ENT")
        print("9-10 ENT")
        print("10-11 PROG")
        print("11-11:30 RECREO")
        print("11:30-12:30 PROG")
        print("12:30-13:30 BBD")
        print("13:30-14:30 BBD")
        print("================================")
    case "JUEVES":
        print("8-9 PROG")
        print("9-10 PROG")
        print("10-11 BBD")
        print("11-11:30 RECREO")
        print("11:30-12:30 BBD")
        print("12:30-13:30 SIST")
        print("13:30-14:30 SIST")
        print("================================")
    case "VIERNES":
        print("8-9 SIST")
        print("9-10 SIST")
        print("10-11 LENG")
        print("11-11:30 RECREO")
        print("11:30-12:30 LENG")
        print("12:30-13:30 PROG")
        print("13:30-14:30 PROG")  
        print("================================")
    case "SABADO":
        print("Día de estudio y reflexión")
    case "DOMINGO":
        print("Día de estudio y reflexión")
    case _ :
        print("VALOR INCORRECTO")



#EJERCICIO2
mes = int(input("Introduce el mes: "))

match mes:
    case 1 | 2 :
        print("Invierno")
    case 3: 
        print("Entre Invierno y Primavera")
    case 4 | 5 :
        print("Primavera")
    case 6:
        print("Entre Primavera y Verano")
    case 7 | 8:
        print("Verano")
    case 9:
        print("Entre Verano y Otoño")
    case 10 | 11:
        print("Otoño")
    case 12 :
        print("Entre Invierno y Otoño")


#EJERCICIO3

print("Habitacion | Camas | Planta")
print("1.Azul | 2 | Primera")
print("2.Roja | 1 | Primera")
print("3.Verde | 3 | Segunda")
print("4.Rosa | 2 | Segunda")
print("5.Gris | 1 | Tercera")

num_hab = int(input("Introduzca un numero de habitacion: "))

match num_hab:
    case 1:
        print("camas: 2")
        print("planta: Primera")

    case 2:
        print("camas: 1")
        print("planta: Primera")

    case 3:
        print("camas: 3")
        print("planta: Segunda")

    case 4:
        print("camas: 2")
        print("planta: Segunda")
        
    case 5:
        print("camas: 1")
        print("planta: Tercera")

#EJERCICIO4
caracter = input("Introduce un caracter: ")
num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

match caracter:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "/":
        print(num1/num2)
    case "*":
        print(num1*num2)

#EJERCICIO6
import random

usuario = input("Introduce Usuario PIEDRA | PAPEL | TIJERAS: ").upper()
maquina= random.randint(0,2)

match maquina:
    case 0:
        maquina = "PIEDRA"
    case 1:
        maquina = "PAPEL"
    case 2:
        maquina = "TIJERAS"


if usuario == "PIEDRA" or usuario == "PAPEL" or usuario == "TIJERAS":
    print(f"usuario: {usuario}")
    print(f"maquina: {maquina}")


    if (usuario == "PIEDRA" and maquina == "TIJERAS")or (usuario == "PAPEL" and maquina == "PIEDRA")or (usuario == "TIJERAS" and maquina == "PAPEL"):
        print("GANA USUARIO")
    elif (maquina == "PIEDRA" and usuario == "TIJERAS")or (maquina == "PAPEL" and usuario == "PIEDRA")or(maquina == "TIJERAS" and usuario == "PAPEL"):
        print("GANA MAQUINA")
    else:
        print("EMPATE")
else:
    print("ERROR!!!")

#EJERCICIO6

#CON MATCH

import random

usuario = input("Introduce Usuario PIEDRA | PAPEL | TIJERAS: ").upper()
maquina= random.randint(0,2)

match maquina:
    case 0:
        maquina = "PIEDRA"
    case 1:
        maquina = "PAPEL"
    case 2:
        maquina = "TIJERAS"

print(f"usuario: {usuario}")
print(f"maquina: {maquina}")

match maquina:
    case "PIEDRA":
        match usuario:
            case "TIJERAS":
                print("GANA MAQUINA")
            case "PAPEL":
                print("GANA USUARIO")
            case "PIEDRA":
                print("EMPATE")
    case "PAPEL":
        match usuario:
            case "TIJERAS":
                print("GANA USUARIO")
            case "PAPEL":
                print("EMPATE")
            case "PIEDRA":
                print("GANA MAQUINA")
    case "TIJERAS":
        match usuario:
            case "TIJERAS":
                print("EMPATE")
            case "PAPEL":
                print("GANA MAQUINA")
            case "PIEDRA":
                print("GANA USUARIO")
"""
























