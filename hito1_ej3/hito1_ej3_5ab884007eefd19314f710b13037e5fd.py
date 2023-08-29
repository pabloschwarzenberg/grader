ingreso=input()
fecha=input()
edad=2017-int(fecha)
hijos=input()
pertenencia=input()
estado=input(str())
lugar=input(str())
if int(pertenencia)>=10 and int(hijos)>=2:
  print("APROBADO")
if estado=="C" and int(hijos)>=3 and 45<int(edad)<55:
  print("APROBADO")
if int(ingreso)>2500000 and estado=="S" and lugar=="U":
  print("APROBADO")
if int(ingreso)>3500000 and pertenencia>=5:
  print("APROBADO")
if lugar=="R" and estado=="C" and int(hijos)<2:
  print("APROBADO")
else:
  print("RECHAZADO")