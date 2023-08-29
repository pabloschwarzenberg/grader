def evaluar_credito(ingreso, nacimiento, hijos, años_banco, estado_civil, ubicacion):
    ingreso = int(ingreso)
    nacimiento = int(nacimiento)
    hijos = int(hijos)
    años_banco = int(años_banco)
    
    if años_banco > 10 and hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and hijos > 3 and nacimiento >= 45 and nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and años_banco > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Ejemplo de uso
ingreso = input("Ingrese el ingreso mensual en pesos: ")
nacimiento = input("Ingrese el año de nacimiento: ")
hijos = input("Ingrese el número de hijos: ")
años_banco = input("Ingrese los años de pertenencia al banco: ")
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese la ubicación (U para urbano, R para rural): ")

resultado = evaluar_credito(ingreso, nacimiento, hijos, años_banco, estado_civil, ubicacion)
print("Resultado:", resultado)
