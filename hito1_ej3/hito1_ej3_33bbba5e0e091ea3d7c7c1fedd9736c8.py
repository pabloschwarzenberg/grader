#Aprobación de Créditos
#Entradas
ingreso = int(input("Ingreso (en pesos):"))
nacimiento = int(input("Año de nacimiento:"))
hijos = int(input("Número de hijos:"))
pertenencia = int(input("Años de pertenencia al banco:"))
estado_civil =(input("Estado civil (S: soltero, C: casado):"))
locacion =(input("Si vive en campo o ciudad (U: urbano, R: rural):"))
S = soltero = estado_civil
C = casado = estado_civil
U = urbano = locacion
R = rural = locacion
edad = nacimiento - 2021
#Procedimiento
if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == S and hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == soltero and locacion == U:
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif locacion == R and estado_civil == casado and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
    
    