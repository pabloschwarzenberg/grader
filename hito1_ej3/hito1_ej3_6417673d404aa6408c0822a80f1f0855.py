#Aprobación de créditos
def evaluar_credito():
    ingreso = int(input("Ingrese su ingreso en pesos: "))
    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos: "))
    anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    tipo_vivienda = input("Ingrese su tipo de vivienda (U para urbano, R para rural): ")

    if anos_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anos_pertenencia > 5:
        return "APROBADO"
    elif tipo_vivienda == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Ejemplo de uso
resultado = evaluar_credito()
print(resultado)
