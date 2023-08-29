#Contestador de celular
ncelular=input("Introduzca su número de celular:")
while len(ncelular)>8:
  ncelular=input("El númer tiene no posee las 8 cifras correspondientes, inténtelo de nuevo: ")
while len(ncelular)<8:
    ncelular=input("El númer tiene no posee las 8 cifras correspondientes, inténtelo de nuevo: ")
hora=int(input("Introduzca la hora en la que realizó la llamada:" ))
if(hora>=0) and (hora<=7):
  print("CONTESTAR")
elif((hora>=19) and hora<=23):
  print("NO CONTESTAR")
else:
  if(hora<14 and hora>7) and str(ncelular[-3])=="9" and str(ncelular[-2])=="0" and str(ncelular[-1])=="9":
    print("CONTESTAR")
  if(hora<14 and hora>7) and str(ncelular[-3])!="9" and str(ncelular[-2])!="0" and str(ncelular[-1])!="9":
    print("NO CONTESTAR")
  if(hora<19 and hora>17) and str(ncelular[0:1])=="8" and str(ncelular[1:2])=="7" and str(ncelular[2:3])=="7":
    print("NO CONTESTAR")
  if(hora<19 and hora>17) and str(ncelular[0:1])!="8" and str(ncelular[1:2])!="7" and str(ncelular[2:3])!="7":
    print("CONTESTAR")    