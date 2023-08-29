ingreso=int(input())
nacimiento=2022 - int(input())
hijos=int(input())
pertenencia=int(input())
estado=input()
vivienda=input()


if hijos>2 or hijos==2 and pertenencia>10:
  print("APROBADO")
if estado == "C" and hijos >3 and nacimiento>45 and nacimiento<55:
  print("APROBADO")
if ingreso> 2500000 or ingreso==2500000 and estado == "S" and vivienda== "U":
  print("APROBADO")
if ingreso>3500000 or ingreso==3500000 and pertenencia>5:
  print("APROBADO")
if vivienda=="R" and estado=="C" and hijos<2:
  print("APROBADO")
print("RECHAZADO")