
ingresos = int(input("ingresos:"))
edad = int(input("año de nacimiento:"))
hijos = int(input("número de hijos:"))
antiguedad = int(input("años de pertencia al banco:"))
estado = input("estado civil S o C:")
vive = input("si vive en campo o ciudad(\"u\": urbano, \"r\": rural):")
ano = 2021-edad

estado = estado.lower()
vive = vive.lower()
condicion = "RECHAZADO"

if ano >= 10 and hijos >= 2:
               condicion = "APROBADO"
if hijos >3 and ano >= 45 and ano <= 55:
               condicion="APROBADO"
if ingresos > 2500000 and estado =="s" and vive =="u":
               condicion = "APROBADO"
if ingresos > 3500000 and antiguedad >5:
               condicion = "APROBADO"
if vive == "r":
      if estado == "c":
        if hijos <= 2:
               condicion = "APROBADO"
if condicion == "APROBADO":
               print(condicion)
else:
               print(condicion)
