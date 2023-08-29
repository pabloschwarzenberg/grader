#Aprobación de créditos
iin=int(input('Ingreso (en pesos): '))
an=int(input("Año de nacimiento: "))
nh=int(input("numero de hijos: "))
ap=int(input("Años de pertenencia al banco: "))
ec=str(input("Estado civil (S: soltero, C, casado): "))
ur=str(input("(U: urbano, R rural): "))
ed=2018-int(an)

if ap>10 and nh>=2:
  print("APROBADO")
if ec=="C" and nh>=3 and ed>=45 and ed<=55:
  print("APROBADO")
if iin>2500000 and ec=="S" and ur=="U":
  print("APROBADO")
if iin>3500000 and ap>5:
  print("APROBADO")
if ur=="R" and ec=="C" and nh<2:
  print("APROBADO")
else:
  print("RECHAZADO")