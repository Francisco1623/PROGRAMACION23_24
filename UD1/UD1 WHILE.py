#suma = 0
#
#for i in range(11):
#    suma += i
#    
#print(suma)

num = int(input("Introduce un numero: "))


for i in range(11):
    if i > 0:
        res = num * i

        print(f"{num} * {i} = {res}")


res = 0
for i in range(11):
    if i > 0:
        res += num

        print(f"{num} * {i} = {res}")

for i in range(0,11,num):
    print(i)








    
        