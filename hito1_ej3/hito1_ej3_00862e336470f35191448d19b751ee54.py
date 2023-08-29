#Aprobación de créditos
ingreso = int(input("Escriba sus ingresos en pesos: "))
nacimiento = int(input("Escriba su año de nacimiento: "))
numero_hijos = int(input("Escriba su número de hijos: "))
tiempo_en_banco = int(input("Escriba sus años de pertenencia al banco: "))
estado_civil = input("Escriba su estado civil(S soltero, C, casado): ")
residencia = input("(u) urbano, (r) rural: ")
edad = 2022 - nacimiento

if tiempo_en_banco > 10 and numero_hijos >= 2:
    print("APROBADO")
if estado_civil == "c" and numero_hijos > 3 and edad>=45 and edad<=55:
    print("APROBADO")
if ingreso > 2500000 and estado_civil == "S" and residencia == "U":
    print("APROBADO")
if ingreso > 3500000 and tiempo_en_banco > 5:
    print("APROBADO")
if residencia == "R" and estado_civil == "C" and numero_hijos < 2:
    print("APROBADO")
