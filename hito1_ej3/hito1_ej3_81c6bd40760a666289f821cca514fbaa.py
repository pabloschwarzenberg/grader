#Aprobación de créditos
ingresos = int(input("Digite sus ingresos: "))
nacimiento = int(input("Digite su año de nacimiento: "))
hijos = int(input("Cantidad de hijos: "))
antiguedad = int(input("Años de pertenencia al banco: "))
estado = str(input("Soltero o casado: "))
residencia = str(input("reside en campo o ciudad? : "))

edad = 2021-nacimiento

if antiguedad > 10 and hijos >= 2:
    print("APROBADO")
elif antiguedad <= 10 and hijos < 2:
    print("RECHAZADO")

if estado == "casado" and hijos > 3 and edad >= 45 or edad >= 55:
    print("APROBADO")
elif estado != "casado" and hijos < 3 and edad < 45:
    print("RECHAZADO")

if ingresos > 250000 and estado == "soltero" and residencia == "ciudad":
    print("APROBADO")
elif ingresos < 250000 and estado != "soltero" and residencia != "ciudad":
    print("RECHAZADO")

if ingresos > 350000 and antiguedad > 5:
    print("APROBADO")
elif ingresos < 350000 and antiguedad < 5:
    input("RECHAZADO")

if residencia == "campo" and estado == "casado" and hijos < 2:
    print("APROBADO")
elif residencia != "campo" and estado != "casado" and hijos > 2:
    print("RECHAZADO")