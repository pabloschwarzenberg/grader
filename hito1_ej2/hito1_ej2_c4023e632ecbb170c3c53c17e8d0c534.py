#Contestador de celular
celular = int(input("Ingrese el su numero celular de 8 digitos: "))
hora = int(input("Ingrese la hora de la llamada: "))

if hora >= 0 and hora <= 7:
    print("Contestar")
elif hora >= 14 and hora < 17 or str(celular)[5:] == "909":
    print("Contestar")
elif hora >= 17 and hora <= 19 and str(celular)[0:3] != "877":
    print("Contestar")
else:
    print("No Contestar")     