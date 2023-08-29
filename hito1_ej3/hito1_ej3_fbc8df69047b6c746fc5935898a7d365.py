#Aprobación de créditos
ingreso = eval(input("ingrese su ingreso en pesos chilenos: "))
año = eval(input("ingrese su año de nacimiento: "))
hijo = eval(input("ingrese cuanto hijos tiene: "))
años_banco = eval(input("ingrese cuentos años lleva en el banco"))
estado_civil = input("si es soltero ingresee S, si es casado ingrese C: ")
casado = str("C")
soltero = str("S")
lugar = input("si vive en el campo ingrese R si vive en la ciudad ingrese U:")
ciudad = str("U")
campo = str("R")
if años_banco > 10 and hijo > 2:
    print("APROBADO")
if estado_civil == casado and hijo > 3 and año <= 1966 and  año >= 1956:
    print("APROBADO")
if ingreso > 2500000 and estado_civil == soltero and lugar == ciudad:
    print("APROBADO")
if ingreso > 3500000 and años_banco > 5:
    print("APROBADO")
if lugar == campo and estado_civil == casado and hijo < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      