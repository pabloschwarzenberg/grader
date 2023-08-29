#Contestador de celular
numero = int(input("Ingrese numero de telefono: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora <= 7:
    print("Contestar")
elif hora >= 8 and hora <= 13:
    if numero % 100 == 9:
        print("Contestar")
    else:
        print("No contestar")
elif hora >= 17 and hora <= 18:
    if numero // 100000 == 877:
        print("No contestar")
    else:
        print("Contestar")
else:
    print("No contestar")