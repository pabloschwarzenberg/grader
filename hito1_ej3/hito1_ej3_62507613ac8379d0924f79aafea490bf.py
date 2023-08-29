ingreso = int(input("ingrese su sueldo:  "))
ano = int(input("ingrese su edad:  "))
hijo = int(input("ingrese la cantidad de hijos que tiene:  "))
banco = int(input("ingrese la cantidad de anos que lleva en este banco:  "))
estado = input("ingrese su estado civil donde S es soltero y C es casado:  ")
casa = input("ingrese U si vive en la ciudad o R si vive afuera de la ciudad:  ")
if (banco>10 and hijo>=2):
  print("APROBADO")
elif (estado=="C" and hijo>3 and ano>=45 and ano<=50):
  print("APROBADO")
elif (ingreso>2500000 and estado=="S" and casa=="U"):
  print("APROBADO")
elif (ingreso>3500000 and banco>5):
  print("APROBADO")
elif (casa=="R" and estado=="C" and hijo<2):
  print("APROBADO")
else:
  print("RECHAZADO")