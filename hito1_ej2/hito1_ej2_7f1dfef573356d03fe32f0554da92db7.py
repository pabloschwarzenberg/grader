#Contestador de celular
n = str(input("Ingrese un numero telefonico: "))
m = int(input("Ingrese hora de la llamada: "))
if 0 < m < 7 :
 print ("CONTESTAR")
elif 7 < m < 14 :
 if n[7] == "9" and n[6] == "0" and n[5] == "9" :
  print ("CONTESTAR")
 else :
  print ("NO CONTESTAR")
elif 17 <= m <= 19 :
 if n[0] == "8" and n[1] == "7" and n[2] == "7" :
  print ("NO CONTESTAR")
 else :
  print ("CONTESTAR")
elif m > 19 :
 print ("NO CONTESTAR")
else :
 print ("NO CONTESTAR")
