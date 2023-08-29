#Aprobación de créditos
ingresos = int(input("De cuanto es su ingreso:"))
año_de_naciemiento = int(input("Ingrese su año de nacimiento:"))
numero_de_hijos = int(input("Ingrese su numero de hijos:"))
años_de_pertenencia = int(input("Ingrese cuantos años lleva en este banco:"))

from datetime import datetime
date = datetime.now()
edad = (date.year - año_de_naciemiento)

escogio_estado = input("Ingrese ""S"" esta Soltero o ""C"" Si esta casado:")

if (escogio_estado == "S"):
    estado_civil = "Soltero"
elif (escogio_estado == "C"):
    estado_civil = "casado"

escogio_locacion = input("Ingrese ""U"" si vive en Ciudad o ""R"" si vive en campo:")

if (escogio_locacion == "U"):
    locacion = "Ciudad"
elif (escogio_locacion == "R"):
    locacion = "Campo"

if (años_de_pertenencia >= 10 and numero_de_hijos >= 2):
    print("APROBADO")
elif (estado_civil == "casado" and edad >= 45 and edad <= 55):
    print("APROBADO")
elif (ingresos >= int(2500000) and estado_civil == "Soltero" and locacion == "Ciudad"):
    print("APROBADO")
elif (ingresos >= int(3500000) and años_de_pertenencia >= 5):
    print("APROBADO")
elif (locacion == "Campo" and estado_civil == "casado" and numero_de_hijos <= 2):
    print("APROBADO")
else:
    print("RECHAZADO")