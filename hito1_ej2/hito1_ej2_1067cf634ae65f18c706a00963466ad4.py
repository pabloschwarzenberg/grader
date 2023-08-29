#Contestador de celular
Ncelular = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora < 7:
  print("CONTESTAR")
elif hora < 14:
  if Ncelular % 1000 == 909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hora >= 17 and hora < 19:
  if Ncelular // 100000 == 877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
else:
  print("NO CONTESTAR")

      