ingresos=int(input("Ingresos mensuales "))
año=int(input("Año nacimiento "))
años=2021-año
hijos=int(input("Numero de hijos "))
cliente=int(input("Años siendo cliente "))
estado=input("Soltero(S) o Casado(C)")
sector=input("Vive en campo(R) o ciudad(U)")
if(hijos>=2 and cliente>=10):
  print("APROBADO")
elif(estado=="C" and hijos>3 and años>45 and años<55):
  print("APROBADO")
elif(ingresos>2500000 and estado=="S" and sector=="U"):
  print("APROBADO")
elif(ingresos>=3500000 and cliente>=5):
  print("APROBADO")
elif(sector=="R" and estado=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")