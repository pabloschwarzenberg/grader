#Cajero Automático
Ingreso = int(input("Ingrese su monto en pesos:"))

AñoNacimiento = int(input("Ingrese su año de nacimiento: "))

NumeroHijos = int(input("Ingrese cantidad de hijos:"))

AñosEnBanco = int(input("Ingrese años de pertenencia al banco: "))

Estado = str(input("Ingrese si es Soltero (S) o casado (C):"))

CampoOCiudad = str(input("Ingrese si vive en campo (R) o ciudad (U):"))



AñoActual = 2022

Edad = AñoActual - AñoNacimiento



if AñosEnBanco > 10 and NumeroHijos >= 2:

  print("APROBADO")



if str(Estado) == "C" and NumeroHijos > 3 and Edad > 45 and Edad < 55:

  print("APROBADO")



if Ingreso > 2500000 and str(Estado) == "S" and str(CampoOCiudad) == "U":

  print("APROBADO")



if Ingreso > 3500000 and AñosEnBanco > 5:

  print("APROBADO")



if str(CampoOCiudad) == "R" and str(Estado) == "C" and NumeroHijos < 2:

  print("APROBADO")   