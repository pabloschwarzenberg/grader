#Aprobación de créditos
#ENTRADA

ingreso = int(input("Ingrese su renta: "))
nacimiento = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese número de hijos: "))
abanco = int(input("Ingrese años de antiguedad en el banco: "))
ecivil = str(input("Ingrese S para soltero o C para casado: "))
ubicacion = str(input("Ingrese U si vive en zona urbana o R si es zona rural: "))
edad = 2021 - nacimiento
C = "C"
S = "S"
U = "U"
R = "R"

#DESARROLLO

if ubicacion == R and ecivil == C and hijos < 2:
    print("APROBADO")
    
if abanco >= 10 and hijos >= 2:
    print("APROBADO")

if ecivil == C and hijos >= 3 and edad >= 45 and edad <= 55:
    print("APROBADO")

if ingreso >= 2500000 and ecivil == S and ubicacion == U:
    print("APROBADO")

if ingreso >= 3500000 and abanco >= 5:
    print("APROBADO")

else:
    print("RECHAZADO")