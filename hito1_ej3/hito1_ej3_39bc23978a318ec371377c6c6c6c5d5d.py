#Aprobación de créditos
ingreso = eval(input("ingrese su ingreso en pesos chilenos: "))
año = eval(input("ingrese su año de nacimiento: "))
hijos = eval(input("ingrese cuantos hijos tiene: "))
años_banco = eval(input("ingrese cuantos años lleva en el banco:"))
estado_civil = (input("si es soltero ingrese S , si es casado ingrese C : "))
casado = str("C")
soltero = str("S")
lugar = (input("si vive en campo ingrese R si vive en ciudad ingrese U: "))
ciudad = str("U")
campo = str("R")
if años_banco > 10 and hijos > 2:
  print("APROBADO")
if estado_civil == casado and hijos > 3 and año <= 1966 and año >= 1956:
  print("APROBADO")
if ingreso > 2500000 and estado_civil == soltero and lugar == ciudad:
  print("APROBADO")
if ingreso > 3500000 and años_banco > 5:
  print("APROBADO")
if lugar == campo and estado_civil == casado and hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")      