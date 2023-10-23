temperatura = float (input("La temperatura de la sala es: "))
if temperatura > 26 : #devuelve True
    print("Encendiendo aire acondicionado")
elif temperatura < 16:
    print("Encendiendo calefacción")
    if temperatura < 0:
        print("ALERTAA!!!")
else: 
  print("Sin acciones")

print("Registrada:"+ str(temperatura))
