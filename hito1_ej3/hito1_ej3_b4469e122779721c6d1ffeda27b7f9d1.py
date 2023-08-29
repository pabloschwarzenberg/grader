#aprobacion de creditos
ingresos=int(input("ingrese ingresos:$"))
nacimiento=int(input("año de nacimiento:"))
numero_hijos=int(input("numero de hijos:"))
a_banco=int(input("años siendo cliente del banco:"))
estado_civil=input("estado civil casado(c)/soltero(s):")
vive_en=input("vives en zona rural(c)/urbana(U):")

edad=2020-nacimiento

if(a_banco>10 and numero_hijos>=2):
  print("APROBADO")
elif(estado_civil==1 and numero_hijos>3 and edad>=45 and edad<=55):
  print("APROBADO")
elif(ingresos>2500000 and estado_civil=="S" and vive_en=="U"):
  print("APROBADO")
elif(ingresos>3500000 and a_banco>5):
  print("APROBADO")
elif(vive_en=="R" and estado_civil== "C" and numero_hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")