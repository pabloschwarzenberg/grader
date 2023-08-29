#Contestador de celularNumero=str(input("Ingrese su numero de telefono: "))
Numero=int(input("Ingrese el numero de telefono: "))
Hora=int(input("Ingrese hora de la llamada: "))
if Hora>0 and Hora<7:
  print("CONTESTAR")
if Hora>19 and Hora<=23:
  print("NO CONTESTAR")
else:
  if Hora>7 and Hora<14 and str(Numero[-3])=="9"and str(Numero[-2])=="0" and str(Numero[-1])=="9":
    print("CONTESTAR")
  if Hora>7 and Hora<14 and str(Numero[-3])!="9" and str(Numero[-2])!="0" and str(Numero[-1])!="9":
    print("NO CONTESTAR")
  if Hora>17 and Hora<19 and str(Numero[0])=="8"and str(Numero[2])=="7" and str(Numero[2])=="7":
    print("NO CONTESTAR")
  if Hora>17 and Hora<19 and str(Numero[0])!="8"and str(Numero[1])!="7" and str(Numero[2])!="7":
    print("CONTESTAR")