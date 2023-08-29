#Contestador de celular
numero = int(input("ingrese numero telefonico:"))
hora = int(input("ingrese hora de la llamada:"))
lista = list(map(int, str(numero)))
if hora <= 7:
    print("CONTESTAR")

elif hora <= 14:
    if lista[5] == 9 and lista[6] == 0 and lista[7] == 9:
        print("CONTESTAR")


    else:
        print("NO CONTESTAR")

elif hora >= 17 and hora <= 19:
    if lista[0] == 8 and lista[1] == 7 and lista[2] == 7:
        print("NO CONTESTAR")

    else:
        print("CONTESTAR")

elif hora > 19:
    print("NO CONTESTAR")

else:
    print("NO CONTESTAR")