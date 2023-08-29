i = int(input("¿Cuanto es su ingreso? "))
n = int(input("En que año nacio? "))
h = int(input("Cuantos hijos tiene? "))
b = int(input("Hace cuantos años pertenece a este banco "))
ec = (input("¿Estado civil?.Responda C:casado o S:soltero "))
v = (input("vive en capo o en ciudad?.Responda U:urbano o R:rural "))
n = 2022 - n

if b > 10 and h >= 2:
  print("APROBADO")
elif h > 3 and n >= 45 and n <= 55:
  print("APROBADO")
elif i > 2500000 and ec == "S" and v == "U" :
  print("APROBADO")
elif i > 3500000 and b > 5:
  print("APROBADO")
elif v == "R" and ec == "C" and h < 2:
  print("APROBADO")
else:
  print("RECHAZADO")
      