print("--------------------------")
print("A) Añadir cliente")
print("B) Mostrar los porcentajes de clientes premium y normales")
print("C) Visualizar todos los cálculos para clientes premium")
print("D) Visualizar todos los cálculos para clientes normales")
print("E) Mostrar el correo de nuestro mejor cliente y el importe")
print("G) Salir")
print("--------------------------")
opcion = "A"

clientes = 0
si_premium = 0
no_premium = 0
porcen_premium = 0
porcen_no_premium = 0
preciomaxpremium = 0
preciomax = 0
cod_articulo_max = ""
cod_articulo_max_n = ""
unimax_si = 0
cod_producto = 0
unimax_no = 0
unimax_todos = 0
correomax = ""

while opcion != "G":

    opcion = input("Introduce la opcion: ").upper()

    if opcion == "A":
        clientes+=1
        premium = input("Introduce S/N: ").upper()
        if premium == "S":
            si_premium+=1
        else:
            no_premium+=1
        correo = input("Introduce el correo: ")

         
        cod_producto = int(input("Introduce el codigo del producto: "))
        while cod_producto > 0:
            

            cod_articulo = input("Introduce el codigo del articulo: ")
            unidades = int(input("Introduce las unidades: "))
            precio = float(input("Introduce el precio del producto: "))
                
            if unidades > unimax_todos:
                unimax_todos = unidades
                correomax = correo
                importe = precio*unidades
            if precio > preciomax:
                preciomax = precio
                if premium == "S":
                    preciomaxpremium = precio
                    cod_articulo_max = cod_articulo
                    unimax_si = unidades
                else:
                    if unidades > unimax_no:
                        unimax_no = unidades
                        cod_articulo_max_n = cod_articulo

            cod_producto = int(input("Introduce el codigo del producto: "))


        print("--------------------------")
        print("A) Añadir cliente")
        print("B) Mostrar los porcentajes de clientes premium y normales")
        print("C) Visualizar todos los cálculos para clientes premium")
        print("D) Visualizar todos los cálculos para clientes normales")
        print("E) Mostrar el correo de nuestro mejor cliente y el importe")
        print("G) Salir")
        print("--------------------------")

        


    if opcion == "B":
        porcen_premium = (si_premium*100)/clientes
        porcen_no_premium = (no_premium*100)/clientes

        print(f"El porcentaje de los clientes premium es: {porcen_premium}%")
        print(f"El porcentaje de los clientes premium es: {porcen_no_premium}%")

        print("--------------------------")
        print("A) Añadir cliente")
        print("B) Mostrar los porcentajes de clientes premium y normales")
        print("C) Visualizar todos los cálculos para clientes premium")
        print("D) Visualizar todos los cálculos para clientes normales")
        print("E) Mostrar el correo de nuestro mejor cliente y el importe")
        print("G) Salir")
        print("--------------------------")

    if opcion == "C":
        porcen_premium = (si_premium*100)/clientes
        print(f"El porcentaje de los clientes premium es: {porcen_premium}%")
        print(f"Importe máximo por pedido: {preciomax} €")
        print(f"El correo del cliente es: {correo}")
        print(f"Datos del articulo más caro de los premiums: cod_art: {cod_articulo_max} unidades: {unimax_si} precio: {preciomaxpremium} €")

        print("--------------------------")
        print("A) Añadir cliente")
        print("B) Mostrar los porcentajes de clientes premium y normales")
        print("C) Visualizar todos los cálculos para clientes premium")
        print("D) Visualizar todos los cálculos para clientes normales")
        print("E) Mostrar el correo de nuestro mejor cliente y el importe")
        print("G) Salir")
        print("--------------------------")
 
    if opcion == "D":
        porcen_no_premium = (no_premium*100)/clientes
        print(f"Porcentaje de los clientes normales: {porcen_no_premium}%")
        print(f"Código de artículo con más ventas´de clientes normales: {cod_articulo_max_n}")

        print("--------------------------")
        print("A) Añadir cliente")
        print("B) Mostrar los porcentajes de clientes premium y normales")
        print("C) Visualizar todos los cálculos para clientes premium")
        print("D) Visualizar todos los cálculos para clientes normales")
        print("E) Mostrar el correo de nuestro mejor cliente y el importe")
        print("G) Salir")
        print("--------------------------")

    if opcion == "E":
        print(f"El correo de nuestro mejor cliente es: {correomax} ,y el importe es de: {importe} €")

        print("--------------------------")
        print("A) Añadir cliente")
        print("B) Mostrar los porcentajes de clientes premium y normales")
        print("C) Visualizar todos los cálculos para clientes premium")
        print("D) Visualizar todos los cálculos para clientes normales")
        print("E) Mostrar el correo de nuestro mejor cliente y el importe")
        print("G) Salir")
        print("--------------------------")


print("Has salido")



