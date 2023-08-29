#Aprobación de créditos
def evaluar_credito():
    ingreso = int(input("Ingrese su ingreso mensual en pesos: "))
    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos que tiene: "))
    anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    tipo_vivienda = input("Ingrese si vive en campo (R) o ciudad (U): ")

    aprobado = False

    if anos_pertenencia > 10 and num_hijos >= 2:
        aprobado = True
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        aprobado = True
    elif ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
        aprobado = True
    elif ingreso > 3500000 and anos_pertenencia > 5:
        aprobado = True
    elif tipo_vivienda == "R" and estado_civil == "C" and num_hijos < 2:
        aprobado = True

    if aprobado:
        print("APROBADO")
    else:
        print("RECHAZADO")


# Ejecutar la función principal
evaluar_credito()
      