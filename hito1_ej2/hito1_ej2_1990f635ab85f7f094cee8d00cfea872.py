#Contestador de celular
print("Contestador de telefono automatico")
Telefono = str(input("Introduzca el numero de telefono (8 numeros):"))
Hora_llamada = int(input("La hora de llamada:"))
if (Hora_llamada <= 7):
    print("CONTESTAR")
else:
    if (Hora_llamada >= 20):
        print("NO CONTESTAR")
    else:
        if (Hora_llamada <= 14 and str(Telefono[-3]) == "9" and str(Telefono[-2]) == "0" and str(Telefono[-1]) == "9"):
            print("CONTESTAR")
        else:
            if (Hora_llamada >= 17 and Hora_llamada <= 19 and str(Telefono[0:1]) == "8" and str(Telefono[1:2]) == "7" and str(Telefono[2:3]) == "7"):
                print("NO CONTESTAR")
            else:
                print("NO CONTESTAR")
