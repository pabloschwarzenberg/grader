#Aprobación de créditos
Ingreso = int(input("Ingreso (en pesos): "))
Nacimiento = int(input("Año de nacimiento: "))
Hijos = int(input("Número de hijos: "))
Pertenencia = int(input("Años de pertenencia al banco: "))
Estado = input('Estado civil ("S": soltero, "C", cadado):' )
Vive = input('Si vive en campo o cuidad ("U": urbano, "R": rural): ')

if (Pertenencia > 10 and Hijos >= 2) or (Estado == "C" and Hijos > 3 and 45 <= Nacimiento <= 55) or (Ingreso > 2500000 and Estado == "S" and Vive == "U") or (Ingreso > 3500000 and Pertenece > 5) or (Vive == "R" and Estado == "C" and Hijos < 2):
   print("APROBADO")
else:
   print("RECHAZADO")