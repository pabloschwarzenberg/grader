#Contestador de celular
numero = int(input("Ingrese el número de teléfono que está llamando: "))

hora = int(input("Ingrese la hora actual (formato de 24 horas): "))


if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora < 14 and numero % 1000 == 909:
    print("CONTESTAR")
elif hora >= 17 and hora < 19:
  if str(numero).startswith("877"):
    print("NO CONTESTAR")
  print("CONTESTAR")
else:
    print("NO CONTESTAR")