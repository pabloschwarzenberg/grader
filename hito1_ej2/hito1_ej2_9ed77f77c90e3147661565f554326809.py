#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))
if hora_llamada >= 0 and hora_llamada <= 7:
    print("Resultado: CONTESTAR") 
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    print("Resultado: CONTESTAR") 
elif hora_llamada >= 17 and hora_llamada < 19 and str(numero_telefonico).startswith("877"):
    print("Resultado:NO CONTESTAR") 
else:
    print("Resultado: NO CONTESTAR")  # En los demás casos, no se contesta
      