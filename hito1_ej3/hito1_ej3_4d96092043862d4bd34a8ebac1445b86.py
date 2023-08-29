pesos=int(input())
naci=int(input())
hijos=int(input())
banco=int(input())
estado=str(input())
vive=str(input())

if banco>10 and hijos>=2:
  print("APROBADO")
if estado=="C" and hijos>3 and naci<=55 and naci>=45:
  print("APROBADO")
if pesos>2500000 and estado=="S" and vive=="U":
  print("APROBADO")
if pesos>3500000 and banco>5:
  print("APROBADO")
if vive=="R" and estado=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO ")
      