n=int(input("Ingresar numero telefonico "))
h=int(input("Ingresar hora de llamada: "))

if h >= 0 and h < 7:
  print("CONTESTAR")
elif h < 14 or n % 100==909:
  print("CONTESTAR")
elif h >= 17 and h < 19 and str(n).startswith('877'):
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")