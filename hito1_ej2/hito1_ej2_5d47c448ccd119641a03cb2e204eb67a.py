#Contestador de celular
#Contestador de celular
Number=str(input("hola adjunte el numero de telefono: "))
hora=int(input("hola adjunte la hora de la llamada:"))
if hora>0 and hora<7:
  print("CONTESTAR")
if hora>19 and hora<=23:
  print("NO CONTESTAR")
else:
  if hora>7 and hora<14 and str(Number[-3])=="9"and str(Number[-2])=="0" and str(Number[-1])=="9":
    print("CONTESTAR")
  if hora>7 and hora<14 and str(Number[-3])!="9" and str(Number[-2])!="0" and str(Number[-1])!="9":
    print("NO CONTESTAR")
  if hora>17 and hora<19 and str(Number[0])=="8"and str(Number[2])=="7" and str(Number[2])=="7":
    print("NO CONTESTAR")
  if hora>17 and hora<19 and str(Number[0])!="8"and str(Number[1])!="7" and str(Number[2])!="7":
    print("CONTESTAR")
