N = int(input("Ingrese año de nacimiento: "))
H = int(input("Ingrese numero de hijos: "))
I = int(input("Ingrese ingresos: "))
A = int(input("Ingrese año de pertenecia al banco: "))
E = str(input("Soltero o Casado: "))
R = str(input("Ingrese donde vive (campo o ciudad): "))

edad = 2021 - N

if A > 10 and H >= 2:
    print("APROBADO")
elif A <= 10 and H < 2:
    print("RECHAZADO")
if E == "casado" and H > 3 and edad >= 45 or edad <= 55:
    print("APROBADO")
elif E!= "casado" and H < 2 and edad < 45 or edad > 55:
    print("RECHAZADO")
if I > 2500000 and E == "soltero" and R == "urbano":
    print("APROBADO")
elif I < 2500000 and E != "soltero" and R != "urbano":
    print("RECHAZADO")
if I > 3500000 and A > 5:
    print("APROBADO")
elif I < 3500000 and A < 5:
    print("RECHAZADO")
if R == "Rural" and E == "casado" and H < 2:
    print("APROBADO")
if R != "Rural" and E != "casado" and H > 2:
    print("RECHAZADO")
    
