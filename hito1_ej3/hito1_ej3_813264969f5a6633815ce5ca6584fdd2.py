def evaluar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion):
    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and 45 <= ano_nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

ingreso = float(input("Ingrese su ingreso mensual en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos que tiene: "))
anos_pertenencia = int(input("Ingrese los años que ha pertenecido al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

resultado = evaluar_credito(ingreso, ano_nacimiento, num_hijos, anos_pertenencia, estado_civil, ubicacion)
print("Resultado:", resultado)
