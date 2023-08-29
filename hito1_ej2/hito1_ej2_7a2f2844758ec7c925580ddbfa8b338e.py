#Contestador de celular
Numero=int(input("Ingrese el numero de Telefono:"))
Llamada=int(input("Ingrese la hora de Llamada:"))
if  (Llamada>=0) or (Llamada<=7):
    print("Contesta! Puede ser una Emergencia")
elif (Llamada<14):
    print("No contestar")
elif (Numero==909):
    print ("contestar")
elif (Llamada>=17) or (Llamada<=19):
    print("contestar")
elif (Numero==877):
    print("No conestar")
elif (Llamada>19):
    print("No contestar")
else:
    print("Te estan Llamando")
