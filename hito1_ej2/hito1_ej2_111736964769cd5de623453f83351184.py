#Contestador de celular
numero_t=int(input("Ingrese numero telefonico:"))
hora=int(input("Ingrese hora de la llamada:"))
num=numero_t%1000
num1=numero_t//100000
if hora>=0 and hora<=7:
 print("CONTESTAR")
if hora>=8 and hora<=14:
 if num==909:
  print ("CONTESTAR")
 else:
  print("NO CONTESTAR")
if hora==15 or hora==16:
 print("NO CONTESTAR")
if hora>=17 and hora<=19:
 if num1==877:
  print("NO CONTESTAR")
 else:
  print ("CONTESTAR")
if hora>=20 and hora<=24:
 print("NO CONTESTAR")
 