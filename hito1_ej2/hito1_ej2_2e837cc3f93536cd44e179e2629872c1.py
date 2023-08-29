#Contestador de celular
telefono=int(input("Ingrese numero telefonico:"))
hora=int(input("Ingrese hora de la llamada:"))
if (9999999 < telefono < 100000000) and (0<= hora <=23):
    if (0<= hora <=7) or ((7<= hora <=14) and (telefono%1000==909)) or ((17<= hora <=19) and (telefono//1000==877)):
        print("Resultado: CONTESTAR")
    elif hora>19:
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")