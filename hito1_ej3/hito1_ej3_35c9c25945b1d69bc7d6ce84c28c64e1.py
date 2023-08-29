#Aprobación de créditos
S = 1
C = 2
U = 3
R = 4
ingresos = int(input("Ingreso (en pesos)="))
nacimiento = int(input("Año de nacimiento="))
hijos = int(input("Número de hijos="))
pertenencia = int(input("Años de pertenencia al banco="))
estado = str(input("Estado civil (S: soltero, C, casado)="))
casa = str(input("Si vive en campo o cuidad (U: urbano, R: rural)="))

edad = 2020 - nacimiento

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado == C and hijos > 3 and 45 <= edad <= 55:
    print("APROBADO")
elif ingresos > 2500000 and estado == S and casa == U:
    print("APROBADO")
elif ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")
elif casa == R and estado == C and hijos < 2:
    print("APROBADO")
else:
    print("APROBADO")

