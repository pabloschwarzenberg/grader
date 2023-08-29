#Contestador de celular
telefono = 0
hora = 0
telefono  = int(input("Ingrese número de teléfono: "))
hora  = int(input("Ingrese hora de la llamada: "))
tel_num_fin = telefono % 1000
tel_num_ini = int(telefono / 100000)

if (hora >= 0 and hora <= 7):
    print("CONTESTAR")
elif(hora >= 8 and hora < 14 and tel_num_fin == 909):
    print("CONTESTAR")
elif(hora >= 17 and hora < 19 and tel_num_ini != 877):
    print("CONTESTAR")
elif (hora > 19):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")   