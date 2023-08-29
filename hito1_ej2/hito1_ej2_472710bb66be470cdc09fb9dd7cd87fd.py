Llamada = str(input("Ingrese su numero de telefono:"))
hora_llamada = int(input("Ingrese la hora de realizar la llamada:"))
if hora_llamada > 0 and hora_llamada < 7:
   print("CONTESTAR")
if hora_llamada > 19 and hora_llamada <= 23:
   print("NO CONTESTAR")
else:
   if hora_llamada > 7 and hora_llamada < 14 and str(Llamada[-3]) == "9" and str(Llamada[-2]) == "0" and str(Llamada[-1]) == "9":
      print("CONTESTAR")
   if hora_llamada > 7 and hora_llamada < 14 and str(Llamada[-3]) != "9" and str(Llamada[-2]) != "0" and str(Llamada[-1]) != "9":
      print("NO CONTESTAR")
   if hora_llamada > 17 and hora_llamada < 19 and str(Llamada[0:1]) == "8" and str(Llamada[1:2]) == "7" and str(Llamada[2:3]) == "7":
      print("NO CONTESTAR")
   if hora_llamada > 17 and hora_llamada < 19 and str(Llamada[0:1]) != "8" and str(Llamada[1:2]) != "7" and str(Llamada[2:3]) != "7":
      print("CONTESTAR")
    
