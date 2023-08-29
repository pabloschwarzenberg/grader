numT = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
list = list(str(numT))
if hora >= 0 and hora <= 7:
    print("Contestar")
elif hora <= 14:
    if list[5] == "9" and list[6] == "0" and list[7] == "9":
        print("Contestar")
    else:
        print("No contestar")
elif hora >= 17 and hora <= 19:
    if list[0] == "8" and list[1] == "7" and list[2] == "7":
        print("No contestar")
    else:
        print("Contestar")
elif hora >= 19:
    print("No contestar")