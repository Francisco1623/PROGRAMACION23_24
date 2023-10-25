n = int(input("Introduce un numero: "))
n_max = 0
cont_repe = 0
n_anterior = 0
repetidos = ""

while n != 0:
    
    
    if (n+1 == n_anterior) or (n == n_anterior) or (n < n_anterior) or (n+1 < n_anterior):
        creciente = "NO está creciente"
    else:
        creciente = "SI está creciente"

    if (n-1 == n_anterior) or (n == n_anterior) or (n > n_anterior) or (n-1 > n_anterior):
        decreciente = "NO está decreciente"
    else:
        decreciente = "SI está decreciente"

    
    if n == n_anterior:
        cont_repe+=1
    else:
        repetidos = "NO hay números repetidos"
    if cont_repe >=1:
        repetidos = "SI hay números repetidos"
    else:
        repetidos = "NO hay números repetidos"
    


            

    

    n_anterior = n
    n = int(input("Introduce un numero: "))


print(creciente)
print(decreciente)
print(repetidos)
