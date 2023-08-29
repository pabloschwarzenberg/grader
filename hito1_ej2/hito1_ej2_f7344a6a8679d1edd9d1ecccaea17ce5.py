#Contestador de celular
n=str(input("hola adjunte el numero de telefono: "))
h=int(input("hola adjunte la hora de la llamada:"))

if h>0 and h<7:
  print("contestar")
if h>19 and h<=23:
  print("no contestar")

else:

  if h>7 and h<14 and str(n[-3])=="9"and str(n[-2])=="0" and str(n[-1])=="9":
    print("contestar")
  if h>7 and h<14 and str(n[-3])!="9" and str(n[-2])!="0" and str(n[-1])!="9":
    print("no contestar")
  if h>17 and h<19 and str(n[0])=="8"and str(n[2])=="7" and str(n[2])=="7":
    print("no contestar")
  if h>17 and h<19 and str(n[0])!="8"and str(n[1])!="7" and str(n[2])!="7":
    print("contestar")  