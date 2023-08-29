nacimiento = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese numero de hijos: "))
ingresos = int(input("Ingrese ingresos: "))
año = int(input("Ingrese año de pertenecia al banco: "))
estado = str(input("Soltero o Casado: "))
residencia = str(input("Ingrese donde vive: "))

edad = 2021 - nacimiento

if año > 10 and hijos >= 2:
    print("APROBADO")
elif año <= 10 and Hi < 2:
    print("RECHAZADO")
if estado == "casado" and hijos > 3 and edad >= 45 or edad <= 55:
    print("APROBADO")
elif estado!= "casado" and hijos < 2 and edad < 45 or edad > 55:
    print("RECHAZADO")
if ingresos > 2500000 and estado == "soltero" and residencia == "urbano":
    print("APROBADO")
elif ingresos < 2500000 and estado != "soltero" and residencia != "urbano":
    print("RECHAZADO")
if ingresos > 3500000 and año > 5:
    print("APROBADO")
elif ingresos < 3500000 and año < 5:
    print("RECHAZADO")
