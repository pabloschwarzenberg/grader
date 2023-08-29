#Contestador de celular
celular = int(input("Ingrese numero telefonico "))
hora = int(input("Ingrese hora de la llamada "))
x = str(celular)
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora <= 14 and hora < 7:
    if x[5] == x[7] == 9 and x[6]== 0:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    if x[0] != 8 and x[1] == x[3] != 7:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 19 and hora <= 23:
        print("NO CONTESTAR")
else:
    print("CONTESTAR")