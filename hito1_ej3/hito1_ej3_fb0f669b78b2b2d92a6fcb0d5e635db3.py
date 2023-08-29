#Aprobación de créditos
N = int(input("Ingrese año de nacimiento: "))

NH = int(input("Ingrese numero de hijos: "))

I = int(input("Ingrese ingresos: "))

AB = int(input("Ingrese año de pertenecia al banco: "))

SC = str(input("Soltero o Casado: "))

V = str(input("Ingrese donde vive: "))

edad = 2021 - N

if AB > 10 and NH >= 2:
    print("APROBADO")
elif AB <= 10 and NH < 2:
    print("RECHAZADO")
if SC == "casado" and NH > 3 and edad >= 45 or edad <= 55:
    print("APROBADO")
elif SC!= "casado" and NH < 2 and edad < 45 or edad > 55:
    print("RECHAZADO")
if I > 2500000 and SC == "soltero" and V == "urbano":
    print("APROBADO")
elif I < 2500000 and SC != "soltero" and V != "urbano":
    print("RECHAZADO")
if I > 3500000 and AB > 5:
    print("APROBADO")
elif I < 3500000 and AB < 5:
    print("REC…")