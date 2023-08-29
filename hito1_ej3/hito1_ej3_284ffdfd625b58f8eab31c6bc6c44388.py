def aprobar_credito():
    ingreso = int(input("Ingrese su ingreso en pesos: "))
    nacimiento = int(input("Ingrese su año de nacimiento: "))
    hijos = int(input("Ingrese el número de hijos que tiene: "))
    pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    ciudad = input("Ingrese U si vive en la ciudad o R si vive en el campo: ")

    if pertenencia > 10 and hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and hijos > 3 and 45 <= (2023 - nacimiento) <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ciudad == "U":
        return "APROBADO"
    elif ingreso > 3500000 and pertenencia > 5:
        return "APROBADO"
    elif ciudad == "R" and estado_civil == "C" and hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

print(aprobar_credito())
