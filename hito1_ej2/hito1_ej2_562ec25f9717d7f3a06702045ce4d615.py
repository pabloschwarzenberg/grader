#Contestador de celular
numero = int(input("Ingrese número de telefono: "))
hora = int(input("Ingrese hora de llamada: "))

if hora >= 0 and hora <= 7:
    print("Contestar")
elif hora < 14:
    if numero[-3:] == "909":
        print("Contestar")
    else:
        print("No Contestar")
elif hora >= 17 and hora <= 19:
    if numero[:3] == "877":
        print("No Contestar")
    else:
        print("Contestar")
    if hora >= 19:
        print("No Contestar")

      