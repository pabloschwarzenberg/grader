#Aprobación de créditos
ingreso=int(input())
ano_nacimiento=int(input())
numero_hijos=int(input())
anos_banco=int(input())
estado=str(input())
vive=str(input())
if numero_hijos>=2:
 if anos_banco>10:
  print("APROBADO")
 else:
  print("REPROBADO")
if 1962<ano_nacimiento<1972:
 if numero_hijos>=3:
  if  estado=="C":
   print("APROBADO")
  else:
   print("REPROBADO")
 else:
  print("REPROBADO")
if ingreso>=2500000:
 if estado=="S":
  if vive=="U":
   print("APROBADO")
  else:
   print("REPROBADO")
 else:
  print("REPROBADO")
if ingreso>=3500000:
 if anos_banco>5:
  print("APROBADO")
 else:
  print("REPROBADO")
if numero_hijos<2:
 if estado=="C":
  if vive=="R":
   print("APROBADO")
  else:
   print("REPROBADO")
 else:
  print("REPROBADO")