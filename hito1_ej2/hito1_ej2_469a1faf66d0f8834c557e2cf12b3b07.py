#Contestador de celular
celular = int(input("ingresa numero telefonico: "))
hora = int(input("ingresa hora de la llamda: "))
ultimo_tres = celular%1000
primeros_tres = celular//100000
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora >=8 and hora <=13:
    if ultimo_tres == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 14 and hora <=16:
    print("NO CONTESTAR")
elif hora >= 17 and hora <=19:
    if primeros_tres == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    if hora >= 20 and hora <= 23:
        print("NO CONTESTAR")