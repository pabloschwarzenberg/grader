#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))


if hora >= 0 and hora <= 7:
    print("Resultado: CONTESTAR")
elif hora >= 14 and hora <17 or str(numero)[5:] == "909":
    print("Resultado: CONTESTAR")
elif hora >= 17 and hora <= 19 and str(numero)[0:3] != "877":
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")      