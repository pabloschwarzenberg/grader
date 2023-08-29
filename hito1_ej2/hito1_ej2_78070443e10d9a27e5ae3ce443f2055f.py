numero=int(input("Ingresar numero "))
hora=int(input("Ingresar hora: "))

if hora >= 0 and hora < 7:
  print("CONTESTAR")
elif hora < 14 or numero % 100==909:
  print("CONTESTAR")
elif hora >= 17 and hora < 19 and str(numero).startswith('877'):
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")