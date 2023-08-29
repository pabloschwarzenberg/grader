#Aprobación de créditos
ingreso = eval(input("Ingrese su sueldo mensual: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese numero de hijos: "))
pbanco = int(input("Ingrese años de pertenencia en el banco: "))
estado_c = input("Ingrese si es soltero o casado con las opciones. S o C: ")
vivienda = input("Ingrese si vive en zona urbana o rural con las opciones. U o R: ")
edad = 2022 - nacimiento

if pbanco > 10 and hijos > 2:
    print("APROBADO")
elif estado_c == "C" and hijos>3 and edad>= 45 and edad<= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_c == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso > 3500000 and pbanco == 5:
    print("APROBADO")
elif vivienda == "R" and estado_c == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")