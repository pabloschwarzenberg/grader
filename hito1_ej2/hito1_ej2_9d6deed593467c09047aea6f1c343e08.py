#Contestador de celular
numero = int(input("Ingrese el número de teléfono: "))
hora = int(input("Ingrese la hora de la llamada (formato 24 horas): "))    
if hora >= 0 and hora <= 7:
  print("CONTESTAR")
elif hora < 14 and numero % 1000 == 909:
  print("CONTESTAR")
elif hora >= 17 and hora < 19 and numero // 1000000 == 877:
  print("CONTESTAR")
elif hora >= 19:
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")      