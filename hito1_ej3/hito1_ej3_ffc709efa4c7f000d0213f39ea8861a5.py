T = int(input("Ingrese año de nacimiento: "))
H = int(input("Ingrese numero de hijos: "))
I = int(input("Ingrese ingresos: "))
S = int(input("Ingrese año de pertenecia al banco: "))
E = str(input("Soltero o Casado: "))
M = str(input("Ingrese donde vive: "))

edad = 2021 - T

if S > 10 and H >= 2:
    print("APROBADO")
elif S <= 10 and H < 2:
    print("RECHAZADO")
if E == "casado" and H > 3 and edad >= 45 or edad <= 55:
    print("APROBADO")
elif E!= "casado" and H < 2 and edad < 45 or edad > 55:
    print("RECHAZADO")
if I > 2500000 and E == "soltero" and M == "urbano":
    print("APROBADO")
elif I < 2500000 and E != "soltero" and M != "urbano":
    print("RECHAZADO")
if I > 3500000 and S > 5:
    print("APROBADO")
elif I < 3500000 and S < 5:
    print("RECHAZADO")
