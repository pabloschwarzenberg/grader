ingresos = int(input("ingresos: "))
año = int(input("año de nacimiento: "))
hijos = int(input("numero de hijos: "))
banco = int(input("años de pertenencia al banco: "))
estado = str(input("estado civil: (S: solttero C: casado): "))
vivienda = str(input("donde vive: (U: urbano R: rural): "))
if (banco >= 10) and (hijos >= 2):
     print("APROBADO")
elif (estado == "C") and (hijos >= 3) and (1965 <= año <= 1975):
     print("APROBADO")
elif (ingresos >= 2500000) and (estado == "S") and (vivienda == "U"):
     print("APROBADO")
elif (ingresos >= 3500000) and (banco >= 5):
     print("APROBADO")
elif (vivienda == "R") and (estado == "C") and (hijos < 2):
     print("APROBADO")
else:
     print("RECHAZADO")
