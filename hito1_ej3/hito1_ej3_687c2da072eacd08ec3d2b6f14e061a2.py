#Aprobación de créditos
I = int(input("Escriba sus Ingresos en Pesos Chilenos: "))
A = int(input("Escriba su año de nacimiento: "))
H = int(input("Ingrese numero de Hijos: "))
B = int(input("años perteneciente al banco: "))
E = input("Ingrese Estado Civil: ")
C = input("Vive en campo o en ciudad?: ")

if B > 10 and H >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
    
if E == "casado" or "C" and (H > 3) and (45 >= A <= 55):
    print("APROBADO")
else:
    print("RECHAZADO")

if (I > 2500000) and (E == "Soltero" or "SOLTERO" or "soltero" or "S") and (C == "ciudad" or "R"):
    print("APROBADO")
else:
    print("RECHAZADO")

if (I > 3500000) and (B > 5):
    print("APROBADO")
else:
    print("RECHAZADO")

if (C == "U" or "campo") and (E == "casado" or "C") and (H < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
