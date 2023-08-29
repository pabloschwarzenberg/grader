#Aprobación de créditos
Ingreso = int(input("Ingrese su monto en pesos chilenos:"))
AñodeNacimiento = int(input("Ingrese su fecha de nacimiento:"))
Númerodehijos = int(input("Ingrese cantidad de hijos:"))
Añossiendocliente = int(input("Ingrese sus años siendo cliente:"))
EstadoCivil = str(input("ingrese si es soltero (S) o casado (C):"))
CampoOCiudad = str(input("ingrese si vive en campo (R) o ciudad (U):"))

AñoActual = 2021
Edad = AñoActual = AñodeNacimiento

if Añossiendocliente >10 and Númerodehijos >=2:
  print("APROBADO") 
if str(EstadoCivil) == "C" and Númerodehijos > 3 and Edad > 45 and Edad < 55:
  print("APROBADO")
if Ingreso > 2500000 and str(EstadoCivil) =="S" and str (CampoOCiudad) =="U":
  print("APROBADO")
if Ingreso > 3500000 and Añossiendocliente > 5:
  print("APROBADO")
if str(CampoOCiudad) == "R" and str(EstadoCivil) and Númerodehijos < 2:
  print("APROBADO")      