Na = int(input("Ingrese año de nacimiento: "))
Hi = int(input("Ingrese numero de hijos: "))
In = int(input("Ingrese ingresos: "))
Añ = int(input("Ingrese año de pertenecia al banco: "))
Es = str(input("Soltero o Casado: "))
Re = str(input("Ingrese donde vive: "))

edad = 2021 - Na

if Añ > 10 and Hi >= 2:
    print("APROBADO")
elif Añ <= 10 and Hi < 2:
    print("RECHAZADO")
if Es == "casado" and Hi > 3 and edad >= 45 or edad <= 55:
    print("APROBADO")
elif Es!= "casado" and Hi < 2 and edad < 45 or edad > 55:
    print("RECHAZADO")
if In > 2500000 and Es == "soltero" and Re == "urbano":
    print("APROBADO")
elif In < 2500000 and Es != "soltero" and Re != "urbano":
    print("RECHAZADO")
if In > 3500000 and Añ > 5:
    print("APROBADO")
elif In < 3500000 and Añ < 5:
    print("RECHAZADO")