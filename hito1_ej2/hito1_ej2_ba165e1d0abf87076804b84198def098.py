#Contestador de celular
numero=input("ingrese número telefónico:")
hora=int(input("ingrese hora de llamada en formato 24 hrs:"))

if hora < 14 and numero [-3]=='9' and numero [-2]=='0' and numero[-1]=='9':
  print ("CONTESTAR")
if hora>0 and hora <7:
  print ("CONTESTAR")
if hora > 19:
  print ("NO CONTESTAR")
if hora > 17 and hora < 19:
  if numero [0]=='8' and numero[1]=='7' and numero[2]=='7':
    print ("NO CONTESTAR")
  else:
    print("CONTESTAR")
    