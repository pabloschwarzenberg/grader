#Aprobación de créditos
def verificar_aprobacion_credito():
    ingreso = int(input("Ingrese su ingreso mensual en pesos: "))
    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    numero_hijos = int(input("Ingrese el número de hijos: "))
    años_pertenencia_banco = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")
    
    if años_pertenencia_banco > 10 and numero_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and numero_hijos > 3 and 45 <= (2023 - año_nacimiento) <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and años_pertenencia_banco > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and numero_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

resultado = verificar_aprobacion_credito()
print("El crédito es:", resultado)

