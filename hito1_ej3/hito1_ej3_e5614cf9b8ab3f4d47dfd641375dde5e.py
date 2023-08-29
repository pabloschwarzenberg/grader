#Aprobación de créditos
ingresos = eval(input("ingrese sus ingresos en (pesos)"))
nacimiento = int(input("ingrese su año de nacimiento: ")) 
hijos = int(input("ingrese el numero de hijos: "))
años_banco = int(input("ingrese los años en el banco: "))
S = str("soltero")
C = str("casado")
edad = 2021 - nacimiento


var_1 = input("si es casado presione la letra c mayuscula y si es soltero la letra s mayuscula: ")
U = str("urbano")
R = str("rural")

var_2 = input("si vive en campo presione la letra r mayuscula y si vive en ciudad la letra u mayuscula: ")
if años_banco > 10 and hijos >= 2:
  print("APROBADO")
else: print("APROBADO")


if C and hijos > 3 and 45 < edad < 55:
  print("APROBADO")
elif ingresos>2500000 and S and U:
  print("APROBADO")

elif ingresos>3500000 and años_banco>5:
  print("APROBADO")
elif R and C and hijos<2:
  print("RECHAZADO")
   