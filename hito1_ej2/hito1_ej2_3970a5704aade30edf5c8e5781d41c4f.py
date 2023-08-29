#ingresar numero de telefono de 8 cifras
NT = str(input("ingresa un numero de telefono: "))
HR = int(input("hora de la llamada: "))
if 0 <= HR <= 7:
    print("CONTESTAR")
if 7 <= HR <= 14 and NT[-3:]== "909":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
if 17 <= HR <= 19 and NT[3:]== "877":
    print("NO CONTESTAR")
else:
    print("CONTESTAR")
if 19 <= HR <= 23:
    print("NO CONTESTAR")