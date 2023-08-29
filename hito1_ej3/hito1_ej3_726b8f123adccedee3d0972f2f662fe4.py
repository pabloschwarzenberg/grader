print("Sistema de Aprovación de Creditos")
I = int(input("Porfavor indiquenos sus ingresos en pesos: "))
A = int(input("Porvafor indiquenos su año de nacimiento: "))
N = int(input("Porvafor indiquenos cuantos hijos tiene: "))
AB = int(input("Porvafor indiquenos cuantos años ha sido miembro de nuestro banco: "))
EC = str(input("Porvafor indiquenos su estado civil, con una 'C' para casado o una 'S' para soltero: "))
V = str(input("Porvafor indiquenos si vive en un ambiente rural con una 'R' o si vive en uno ambiente urbano con una 'U': "))

if AB > 10 and N > 2:
  print("estado del credito: APROBADO")
elif EC == "C" and N > 3 and 2022 - A >= 45 and 2022 - A <= 55:
  print("estado del credito: APROBADO")
elif I > 2500000 and EC == "S" and V == "U":
  print("estado del credito: APROBADO")
elif AB > 5 and I > 3500000:
  print("estado del credito: APROBADO")
elif N < 2 and EC == "C" and V == "R":
  print("estado del credito: APROBADO")
else:
  print("estado del credito: RECHAZADO")
  