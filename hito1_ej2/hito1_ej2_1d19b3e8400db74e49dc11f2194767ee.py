#Contestador de celular
numero_telefonico=int(input("Ingrese el numero telefonico: "))
hora_llamada=int(input("Ingrese la hora de la llamada: "))

if hora_llamada>=0 and hora_llamada<=7:
    print("CONTESTAR")
elif hora_llamada<14 and numero_telefonico%1000==909:
    print("CONTESTAR")
elif hora_llamada>=17 and hora_llamada<=19 and numero_telefonico//1000000==877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR ")      