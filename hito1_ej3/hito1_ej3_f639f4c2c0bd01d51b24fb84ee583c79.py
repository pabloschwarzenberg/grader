#Aprobación de créditos
i=int(input("ingreso:"))
an=int(input("año nacimiento:"))
nh=int(input("número de hijos:"))
ap=int(input("años pertenencia:"))
ec=input("estado civil (S:soltero, C:casado):")
ur=input("U:urbano, R:rural : ")
a=2018
if ap>10 and nh>=2:
  print("APROBADO")
elif ec=="C" and nh>3 and 45<(a-an)<55:
  print("APROBADO")
elif i>2500000 and ac=="S" and ur=="U":
  print("APROBADO")
elif i>3500000 and ap>5:
  print("APROBADO")
elif ur=="R" and ec=="C" and nh<2:
  print("APROBADO")
else:
  print("RECHAZADO")