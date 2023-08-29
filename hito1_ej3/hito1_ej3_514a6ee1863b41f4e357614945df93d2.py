#Aprobación de créditos
Ingreso=int(input("Indique monto a evaluar:"))
Nacimiento=int(input("Usted nacio el año:"))
NumeroHijos=int(input("¿Cuantos hijos tiene?:"))
AnBanco=int(input("Usted ingreso al banco el año:"))
Estado=str(input("Si es soltero ingrese (S) y si es casado (C):"))
CampoOCiudad=str(input("Ingrese si vive en campo (R) o ciudad (U):"))

#Parametros, condiciones y Strings
Actual=2022
Edad=Actual-Nacimiento
if AnBanco>10 and NumeroHijos>=2:
  print("APROBADO")
if str(Estado) == "C" and NumeroHijos > 3 and Edad > 45 and Edad < 55:
  print("APROBADO")
if Ingreso > 2500000 and str(Estado) == "S" and str(CampoOCiudad) == "U":
  print("APROBADO")
if Ingreso > 3500000 and AnBanco > 5:
  print("APROBADO")
if str(CampoOCiudad) == "R" and str(Estado) == "C" and NumeroHijos < 2:
  print("APROBADO")      