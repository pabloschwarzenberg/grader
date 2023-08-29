#Aprobación de créditos
i=int(input("ingreso (en pesos):"))
an=int(input("año de nacimiento:"))
nh=int(input("número de hijos:"))
ap=int(input("años de pertenencia al banco:"))
ec=input("¿Cuál es su estado civil? (S) soltero; (C) casado:")
v=input("vive en campo (R) o ciudad (U):")
e=(2020-an)
if((ec=="C") and (nh>3) and (45<e<55)) or ((ap>10) and (nh>=2)) or ((i>2500000) and (ec=="S") and (v=="U")) or ((i>3500000) and (ap>5)) or ((v=="R") and (ec=="C") and (nh<2)):
  print("APROBADO")
else:
  print("RECHAZADO")