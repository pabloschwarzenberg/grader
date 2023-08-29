#Aprobación de créditos
ingresos = int(input("Digite sus ingresos: "))
nacimiento = int(input("Digite su año de nacimiento: "))
hijos = int(input("Cantidad de hijos: "))
añosbanco = int(input("Años de pertenencia al banco: "))
estadocivil = str(input("Soltero o casado: "))
residencia = str(input("reside en campo o ciudad? : "))

edad = 2021-nacimiento

if añosbanco > 10 and hijos >= 2:
    print("APROBADO")
elif añosbanco <= 10 and hijos < 2:
    print("RECHAZADO")

if estadocivil == "casado" and hijos > 3 and edad >= 45 or edad >= 55:
    print("APROBADO")
elif estadocivil != "casado" and hijos < 3 and edad < 45:
    print("RECHAZADO")

if ingresos > 250000 and estadocivil == "soltero" and residencia == "ciudad":
    print("APROBADO")
elif ingresos < 250000 and estadocivil != "soltero" and residencia != "ciudad":
    print("RECHAZADO")

if ingresos > 350000 and añosbanco > 5:
    print("APROBADO")
elif ingresos < 350000 and añosbanco < 5:
    input("RECHAZADO")

if residencia == "campo" and estadocivil == "casado" and hijos < 2:
    print("APROBADO")
elif residencia != "campo" and estadocivil != "casado" and hijos > 2:
    print("RECHAZADO")      