#Contestador de celular
numero_telefono = str(input("Indique su numero telefonico: "))
hora_llamada = int(input("Indique su hora de llamada: "))
numero_telefono3F = numero_telefono[5:8]
numero_telefono3I = numero_telefono[0:3]
if hora_llamada >= 0 and hora_llamada <= 7:
    print("contestar")
elif hora_llamada > 7 and hora_llamada < 14 and numero_telefono3F == "909":
    print("contestar")
elif not(numero_telefono3I == "877") and hora_llamada >= 17 and hora_llamada <= 19 :
    print("contestar")
elif hora_llamada > 19:
    print("no contestar")
else:
    print("no contestar")
