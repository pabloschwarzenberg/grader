#Aprobación de créditos
ingreso=input("ingreso (pesos)")
nacimiento=input("año de nacimiento")
hijos=input("numero de hijos")
pertenencia=input("Años de pertenencia al banco")
civil=input("Estado civil ('S': soltero, 'C', casado)")
lugar=input("campo o cuidad ("U": urbano, "R": rural)")
ingreso=int(ingreso)
nacimiento=2017-int(nacimiento)
hijos=int(hijos)
pertenencia=int(pertenencia)
if pertenencia>10 and hijos>=2:
  print("APROBADO")
elif civil=="C" and hijos>3 and nacimiento>45 and nacimiento>55:
  print("APROBADO")
elif ingreso>2500000 and civil=="S" and lugar=="U":
  print("APROBADO")
elif ingreso>3500000 and pertenencia>5:
  print("APROBADO")
elif lugar=="R" and civil=="C" and hijos<2:
  print("APROBADO")
else:
  print("NO APROBADO")