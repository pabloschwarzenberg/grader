#Contestador de celular
telefono = 0
hora = -1
while len(str(telefono)) != 8:
    telefono = int(input("Numero telefónico de la llamada 8 digitos : "))
while hora<0 or hora>23:
    hora=int(input("Hora de la llamada en formato de 24 Hrs: "))
if hora >= 0 and hora < 7:
    print("Contestar")
elif hora >= 7 and hora < 14:
    if str(telefono)[5:] == "909":
        print("Contestar")
    else:
        print("No Contestar")
elif hora >= 14 and hora < 17:
    if str(telefono)[0:3] == "877":
        print("Contestar")
    else:
        print("No Contestar")
elif hora >= 17 and hora < 19:
    if str(telefono)[0:3] == "877":
        print("No Contestar")
    else:
        print("Conteste")
elif hora >= 19 and hora < 23:
    print("No Contestar")     