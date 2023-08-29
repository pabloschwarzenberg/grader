#Aprobación de créditos
#Ingreso (en pesos)
#Año de nacimiento
#Número de hijos
# Años de pertenencia al banco
#Estado civil ("S": soltero, "C", casado)
#Si vive en campo o cuidad ("U": urbano, "R": rural)

i = eval(input("Ingreso (en pesos): "))
an = eval(input("Año de nacimiento: "))
nh = eval(input("Número de hijos: "))
ap = eval(input("Años de pertenencia al banco: "))
ec = input("Estado civil (S: soltero, C: casado): ")
v = input("U: urbano, R: rural: ")






if ap > 10 and nh >= 2:
  print("APROBADO")
elif ec == "C" and nh >= 3 and (an >= 1965 and an <= 1975):
  print("APROBADO")
elif i > 25000000 and ec == "S" and v == "U":
  print("APROBADO")
elif i > 3500000 and ap > 5:
  print("APROBADO")
elif v == "R" and ec == "C" and nh < 2:
  print("APROBADO")
else:
  print("REPROBADO")
 