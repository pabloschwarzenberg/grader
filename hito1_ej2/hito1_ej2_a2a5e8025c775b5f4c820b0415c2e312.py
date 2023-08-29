numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora <= 7:
  print("CONTESTAR")
if hora < 14 and numero % 1000 == 909:
   print("CONTESTAR")
  
if hora >= 17 and hora <= 19 and numero //100000 == 877:
  print("NO CONTESTAR")
 
if hora > 19:
   print("NO CONTESTAR")

