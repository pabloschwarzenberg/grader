#Aprobación de créditos
ingreso= int(input("Ingrese su ingreso mensual:"))
AnoN= int(input("Ingrese su año de nacimiento:"))
hijos= int(input("Ingrese numero de hijos:"))
AnosBa= int(input("Ingrese años de pertenencia en el banco:"))
EstadoC= str(input("Ingrese estado civil(S: soltero,C: casado):"))
C = EstadoC
S = EstadoC
CamCiu= str(input("Ingrese si vive en ciudad o campo(U:urbano, R: rural):"))
U = CamCiu
R = CamCiu
anos= 2022 - AnoN


if AnosBa < 10 and hijos >= 2:
    print("AROBADO")

elif (EstadoC==C) and hijos > 3 and anos >= 45 or anos <=55:
    print("APROBADO")


elif ingreso > 2500000 and EstadoC == S and CamCiu == U:
    print("APROBADO")

elif ingreso > 3500000 and AnosBa > 5:
    print("APROBADO")


elif CamCiu == R and EstadoC == C and hijos < 2:
    print("APROBADO")

else: print("RECHAZADO")     