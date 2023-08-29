#Aprobación de créditos
ingreso=int(input("ingreso: "))
ano=int(input("año de nacimiento" ))
hijos=int(input("numero de hijos: "))
pertenencia=int(input("años de pertenencia en el banco"))
estado=input("estado civil: ")
hogar=input("campo o ciudad: ")
if pertenencia>=10 and hijos>=2:
  print("APROBADO")
elif estado=="C" and hijos>=4 and int(2016-ano)>=45 and int(2016-ano)<55:
  print("APROBADO")
elif ingreso>=2500000 and estado=="S" and hogar=="U":
  print("APROBADO")
elif ingreso>=3500000 and pertenencia>5:
  print("APROBADO")
elif hogar=="R" and estado=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")
