#Aprobación de créditos
ingresos = int(input("Ingresos :$"))
ano = int(input("Ingrese año de nacimiento:"))
hijos = int(input("Cantidad de hijos:"))
antiguedad = int(input("Años de antiguedad en el banco :"))
estado = input("Estado Civil S o C :")
vive = input("Si vive en campo o ciudad (\"U\": urbano, \"R\": rural)")
ano = 2020 - ano

estado = estado.lower()
vive = vive.lower()
aprobado = "RECHAZADO"

if ano >= 10 and hijos >= 2:
    aprobado = "APROBADO"
if hijos >3 and ano >= 45 and ano <=55:
    aprobado = "APROBADO"
if ingresos >250000 and estado =="s" and vive =="u":
    aprobado = "APROBADO"
if ingresos >350000 and antiguedad >55:
    aprobado = "APROBADO"
if vive == "r":
    if estado == "c":
       if hijos <=2:
          aprobado = "APROBADO"
if aprobado == "APROBADO":
   print(aprobado)
else:
    print(aprobado)
   