#Aprobación de créditos

I = int(input("Tenga el agrado de indicar sus ingresos en pesos: "))
A = int(input("Tenga el agrado de indicar su año de nacimiento: "))
H = int(input("Tenga el agrado de indicar cuantos hijos tiene: "))
MB = int(input("Tenga el agrado de indicar por cuantos años ha sido miembro del banco: "))
EC = str(input("Tenga el agrado de indicar su estado civil, con una 'C' para casado o una 'S' para soltero: "))
E = str(input("Tenga el agrado de indicar si vive en un entorno rural con una 'R' o si vive en un entorno urbano con una 'U': "))

if MB > 10 and H > 2:
  print("estado del credito: APROBADO")
elif EC == "C" and H > 3 and 2022 - A >= 45 and 2022 - A <= 55:
  print("estado del credito: APROBADO")
elif I > 2500000 and EC == "S" and E == "U":
  print("estado del credito: APROBADO")
elif MB > 5 and I > 3500000:
  print("estado del credito: APROBADO")
elif H < 2 and EC == "C" and E == "R":
  print("estado del credito: APROBADO")
else:
  print("estado del credito: RECHAZADO")