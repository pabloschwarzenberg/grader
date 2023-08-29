ingreso = float(input("Ingreso: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
banco = int(input("Años de pertenencia al banco: "))
S = 1
U = 1
C = 0
R = 0
estado = eval(input("Estado Civil? (S/C): "))
zona = eval(input("Vive en zona Urbana o Rural? U/R: "))
edad = 2020-nacimiento
if banco > 10 and hijos >= 2:
  print ("APROBADO")
if hijos > 3 and edad >= 45 and edad <= 55:
  print ("APROBADO")
if ingreso > 2500000 and estado == 1 and zona == 1:
  print ("APROBADO")
if ingreso > 3500000 and banco > 5:
  print ("APROBADO")
if zona == 0 and estado == 0 and hijos < 2:
  print ("APROBADO")
else:
  print ("RECHAZADO")