Numero_Telefono = str(input("Indique su numero telefonico: "))
Hora_llamada = int(input("Indique su hora de llamada: "))
Numeros_finales = Numero_Telefono[5:8]
Numeros_iniciales = Numero_Telefono[0:3]
if Hora_llamada >= 0 and Hora_llamada<= 7:
    print("CONTESTAR,POSIBLE LLAMADO DE EMERGENCIA")
elif Hora_llamada > 7 and Hora_llamada < 14 and Numeros_finales == "909":
    print("CONTESTAR")
elif not(Numeros_iniciales == "877") and Hora_llamada >= 17 and Hora_llamada <= 19 :
    print("CONTESTAR")
elif Hora_llamada > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
