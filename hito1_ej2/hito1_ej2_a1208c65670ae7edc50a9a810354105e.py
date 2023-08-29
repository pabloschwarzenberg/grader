#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

if hora_llamada >= 0 and hora_llamada <= 7:
    print("Resultado: CONTESTAR")  # Si es entre 00:00 y 07:00, se contesta
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    print("Resultado: CONTESTAR")  # Si es antes de las 14:00 y termina en 909, se contesta
elif hora_llamada >= 17 and hora_llamada < 19 and str(numero_telefonico).startswith("877"):
    print("Resultado: NO CONTESTAR")  # Si es entre 17:00 y 19:00 y comienza por 877, se contesta
else:
    print("Resultado: NO CONTESTAR")  # En los demás casos, no se contesta