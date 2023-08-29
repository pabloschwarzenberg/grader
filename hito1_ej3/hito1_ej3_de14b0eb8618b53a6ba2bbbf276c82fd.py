#Aprobación de créditos
ingresos=int(input())
nacimiento=int(input())
hijos=int(input())
agnos=int(input())
civil=input()
vive=input()
if agnos>10 and hijos>=2:
  print("APROBADO")
elif civil=="C" and hijos>3 and 45<=agnos<=55:
  print("APROBADO")
elif ingresos>2500000 and civil=="S" and vive=="U":
  print("APROBADO")
elif ingresos>3500000 and agnos>5:
  print("APROBADO")
elif vive=="R" and civil=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")
