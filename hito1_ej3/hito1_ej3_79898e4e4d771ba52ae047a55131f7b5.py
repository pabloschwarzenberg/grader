#Aprobación de créditos
variable1 = int(input("Ingreso (en pesos): "))
variable2 = int(input("Año de nacimineto: "))
variable3 = int(input("Número de hijos: "))
variable4 = int(input("Años de pertenencia al banco: "))
variable5 = (input("Estado civil (S = soltero, C = casado)"))
variable6 = (input("Vive en campo o ciudad (U = urbano, R = rural)"))
if (variable4 > 10) and (variable3 >= 2):
    print("APROBADO")
if (variable5 == "VARIABLE3") and (variable > 3) and (1966 <= variable2) and  (variable2 <= 1976):
    print("APROBADO")
if (variable1 > 2500000) and (variable5 == "S") and (varaible6 == "U"):
    print("APROBADO")
if (variable1 > 3500000) and (variable4 > 5):
    print("APROBADO")
if (variable6 == "R") and (variable5 == "C") and (variable3 < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
      