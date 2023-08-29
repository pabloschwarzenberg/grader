#Contestador de celular
#ENTRADA
cel = int(input("Ingrese el numero de telefono: "))
hora = int(input("Ingresa la hora de la llamada: "))

#PROCESO
if (hora >= 0 and hora <= 7):
    print("CONTESTAR")
elif (hora <= 14) and (cel % 1000) == 909:
    print("CONTESTAR")
elif (hora > 18 and hora < 19) :
    print("CONTESTAR")
elif (hora > 19):
    print("NO CONTESTAR")
elif (hora >= 8 and hora <= 13):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")