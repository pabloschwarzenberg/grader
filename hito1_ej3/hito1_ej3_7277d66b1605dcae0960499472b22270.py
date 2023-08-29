#Aprobación de créditos
ingreso = int(input("Ingrese sus ingresos: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Número de hijos: "))
pertenece = int(input("Años de pertenencia al banco: "))
estado = input("Estado civil (S: Soltero, C: Casado): ")
vive = input("Vive en ciudad o campo (U: Urbano, R: Rural): ")

def aprobar_credito(ingreso, nacimiento, hijos, pertenece, estado, vive):
    if pertenece > 10 and hijos >= 2:
        return "APROBADO"
    elif estado == "C" and hijos > 3 and 45 <= (2023 - nacimiento) <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado == "S" and vive == "U":
        return "APROBADO"
    elif ingreso > 3500000 and pertenece > 5:
        return "APROBADO"
    elif vive == "R" and estado == "C" and hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

resultado = aprobar_credito(ingreso, nacimiento, hijos, pertenece, estado, vive)
print(resultado)