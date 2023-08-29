#Contestador de celular
num=str(input("Ingrese el número de teléfono: "))
hora=int(input("Ingrese la hora de llamada:"))
if hora>0 and hora<7:
  print("Contestar")
if hora>19 and hora<=23:
  print("No contestar")
else:
  if hora>7 and hora<14 and str(num[-3])=="9"and str(num[-2])=="0" and str(num[-1])=="9":
    print("Contestar")
  if hora>7 and hora<14 and str(num[-3])!="9" and str(num[-2])!="0" and str(num[-1])!="9":
    print("No contestar")
  if hora>17 and hora<19 and str(num[0])=="8"and str(num[2])=="7" and str(num[2])=="7":
    print("No contestar")
  if hora>17 and hora<19 and str(num[0])!="8"and str(num[1])!="7" and str(num[2])!="7":
    print("Contestar")