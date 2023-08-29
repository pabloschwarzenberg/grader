#Contestador de celular
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_de_la_llamada = int(input("Ingrese hora de la llamada: "))
if hora_de_la_llamada >= 0 and hora_de_la_llamada < 7:
    print("CONTESTAR")
elif hora_de_la_llamada == 13:
    print("contestar")
elif hora_de_la_llamada < 14 and numero_telefonico % 100 == 909:
    print("CONTESTAR")
elif hora_de_la_llamada >= 17 and hora_de_la_llamada < 19 and not str(numero_telefonico).startswith("877"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")     