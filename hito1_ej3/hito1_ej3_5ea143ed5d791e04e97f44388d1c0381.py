#Aprobación de créditos
#se definen las variables
a = int(input("ingreso (en pesos): "))
b = int(input("Año de nacimineto: "))
c = int(input("número de hijos: "))
d = int(input("Años de pertenencia al banco: "))
e = (input("estado civil (S = soltero, C = casado)"))
f = (input("vive en campo o ciudad (U = urbano, R = rural)"))


# se procesan los datos y se ven las condiciones 
if (d > 10) and (c >= 2):
    print("APROBADO")
if (e == "C") and (c > 3) and (1966 <= b) and  (b <= 1976):
    print("APROBADO")
if (a > 2500000) and (e == "S") and (f == "U"):
    print("APROBADO")
if (a > 3500000) and (d > 5):
    print("APROBADO")
if (f == "R") and (e == "C") and (c < 2):
    print("APROBADO")
else:
    print("RECHAZADO")