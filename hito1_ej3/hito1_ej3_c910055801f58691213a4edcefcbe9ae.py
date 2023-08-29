# Aprobación de créditos
I = int(input("Ingreso (en pesos) >>> "))
N = 2022 - int(input("Año de nacimiento >>> "))
H = int(input("Número de hijos >>> "))
A = int(input("Años de pertenencia al banco >>> "))
SC = input("Estado civil (S/C) >>> ")
while SC != "S" and SC != "C":
    print("Entrada inválida")
    SC = input("Estado civil (S/C) >>> ")
UR = input("Residencia urbana o rural (U/R) >>> ")
while UR != "U" and UR != "R":
    print("Entrada inválida")
    UR = input("Residencia urbana o rural (U/R) >>> ")

APROBADO = False
if A > 10 and H >= 2:
    APROBADO = True
elif SC == "C" and H > 3 and 45 <= N <= 55:
    APROBADO = True
elif I > 2500000 and SC == S and UR == U:
    APROBADO = True
elif UR == "R" and SC == "C" and H < 2:
    APROBADO = True

if APROBADO == True:
    print("APROBADO")
else:
    print("RECHAZADO")