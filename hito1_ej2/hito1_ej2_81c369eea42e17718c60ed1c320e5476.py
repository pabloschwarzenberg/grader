#Contestador de celular
telefono = (input("Ingrese el numero telefonico: "))
numero = telefono
hora = int(input("Ingrese hora de la llamda (numero entero entre 0 y 23): "))

if (hora >= 0) and (hora <= 7):
    print("CONTESTAR")
elif (hora < 14) and (numero[5:] == "909"):
    print("CONTESTAR")
elif (hora < 14) and (numero[5:] != "909"):
    print("NO CONTESTAR")
elif ((hora >= 17) and (hora <= 19)) and (numero[0:3] == "877"):
    print("NO CONTESTAR")
elif ((hora >= 17) and (hora <= 19)) and (numero[0:3] != "877"):
    print("CONTESTAR")
elif hora > 19:
    print("NO CONTESTAR")
