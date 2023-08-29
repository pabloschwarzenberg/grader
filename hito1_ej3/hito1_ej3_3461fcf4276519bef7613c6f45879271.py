def aprobacion(ingreso, año, n_hijos, años_pertenencia, estado_civil, localia):
    año_actual = 2023
    if años_pertenencia > 10 and n_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and n_hijos > 3 and (45 <= (año_actual - año) <= 55):
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and localia == "U":
        return "APROBADO"
    elif ingreso > 3500000 and años_pertenencia > 5:
        return "APROBADO"
    elif localia == "R" and estado_civil == "C" and n_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

ingreso = int(input("Ingrese su ingreso (en pesos): "))
año = int(input("Ingrese su año de nacimiento: "))
n_hijos = int(input("Ingrese el número de hijos: "))
años_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil ('S' si está soltero y 'C' si está casado): ")
localia = input("Ingrese su localia ('U' para urbano o 'R' para rural): ")

resultado = aprobacion(ingreso, año, n_hijos, años_pertenencia, estado_civil, localia)
print(resultado)