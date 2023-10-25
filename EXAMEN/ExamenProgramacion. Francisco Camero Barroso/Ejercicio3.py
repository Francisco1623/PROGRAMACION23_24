#EJERCICIO 3.1

incidente = input("Desea introducir un nuevo inciedente S/N: ").upper()

n_incidente = 0
i_leve = 0
i_moderado = 0
i_grave = 0
i_eso = 0
i_post = 0
while incidente != "N":
    n_incidente+=1
    tipo = input("El tipo de incidente: Leve(L), Moderado(M) o Grave(G) (L/M/G): ").upper()
    if tipo == "L":
        i_leve+=1
    elif tipo == "M":
        i_moderado+=1
    elif tipo == "G":
        i_grave+=1
    else:
        print("ERROR")

    nivel = input("El nivel en el que se produce, ESO(E) o Post-Obligatoria(P): ").upper()

    if nivel == "E":
        i_eso+=1
    elif nivel == "P":
        i_post+=1
    else:
        print("ERROR")

    incidente = input("Desea introducir un nuevo inciedente S/N: ").upper()
print("No hay incidentes")

porc_eso = (i_eso/n_incidente)*100
porc_post = (i_post/n_incidente)*100

#EJERCICIO 3.2
print(f"Se han producido {n_incidente} incidentes en el centro: {i_leve} de ellos leves, {i_moderado} Moderados y {i_grave} Graves, siendo el {porc_eso}% en ESO y el {porc_post}% en POST_Obligatoria.")
