#Aprobación de créditos
S = 1
C = 2
U = 3
R = 4

Ingreso = eval(input("ingresa tu ingreso en pesos: "))
ano_nacimiento =  eval(input("ingrese su año de nacimiento: "))
cantidad_hijos = eval(input("ingrese cantidad de hijos: "))
anos_banco = eval(input("ingrese años de permanencia al banco: "))
print("1 = soltero")
print("2 = casado")
estado_civil = eval(input("ingrese estado civil: "))
print("3 = urbano")
print("4 = rural")
Ciudad = eval(input("usted vive en: "))
Edad = 2020 - ano_nacimiento

if 10 < anos_banco:
    if 2 <= cantidad_hijos:
        print("APROBADO")

if estado_civil == C:
    if 3 <= cantidad_hijos:
        if 45 <= Edad <= 55:
            print("APROBADO")

if Ingreso > 2500000:
    if estado_civil == S:
        if Ciudad == U:
            print("APROBADO")

if Ingreso > 3500000:
    if anos_banco > 5:
        print("APROBADO")
        
if Ciudad == 4:
    if estado_civil == 2:
        if 2 > cantidad_hijos:
            print("APROBADO")
else:
    print("RECHAZO")
   