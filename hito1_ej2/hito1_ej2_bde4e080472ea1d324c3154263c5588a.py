#Contestador de celular

numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (formato 24 horas): "))

if hora_llamada >= 0 and hora_llamada <= 7 or (hora_llamada < 14 and numero_telefonico % 100 == 909) or (hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico).startswith("877")):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
