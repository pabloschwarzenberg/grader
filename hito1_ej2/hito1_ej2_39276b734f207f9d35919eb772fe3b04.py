#Contestador de celular
telefono = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))


if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora >= 14 and hora <17 or str(telefono)[5:] == "909":
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and str(telefono)[0:3] != "877":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")