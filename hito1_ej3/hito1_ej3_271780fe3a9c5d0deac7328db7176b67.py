ingreso = int(input("Ingrese la cantidad de ingreso en pesos: "))
año_nacimiento = int(input("Ingrese el año de nacimiento: "))
numero_hijos = int(input("Ingrese numero de hijos: "))
años_pertenencia_banco = int(input("Ingrese los años de pertenencia en el banco: "))
estado_civil = str(input("Ingrese su estado civil: "))
lugar_donde_vive = str(input("Ingrese si vive en campo o ciudad: "))
edad = 2023 - año_nacimiento

if años_pertenencia_banco > 10 and numero_hijos >= 2:
    print("Credito APROBADO")

elif estado_civil == "C" and numero_hijos > 3 and 45 < edad < 55:
    print("Credito APROBADO")

elif ingreso > 2500000 and estado_civil == "S" and lugar_donde_vive == "U":
    print("Credito APROBADO")

elif ingreso > 3500000 and años_pertenencia_banco > 5:
    print("Credito APROBADO")

elif lugar_donde_vive == "R" and estado_civil == "C" and numero_hijos < 2:
    print("Credito APROBADO")

else:
    print("Credito RECHAZADO")