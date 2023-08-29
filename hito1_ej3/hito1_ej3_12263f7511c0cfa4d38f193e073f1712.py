#Aprobación de créditos
def verificar_aprobacion():
    ingreso = float(input("Ingrese su ingreso mensual: $"))
    anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos: "))
    anios_pertenencia = int(input("Ingrese el número de años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    tipo_vivienda = input("Ingrese si vive en ciudad (U para urbano) o en campo (R para rural): ")

    if anios_pertenencia > 10 and num_hijos >= 2:
        print("APROBADO")
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
        print("APROBADO")
    elif ingreso > 2500000 and estado_civil == "S" and tipo_vivienda == "U":
        print("APROBADO")
    elif ingreso > 3500000 and anios_pertenencia > 5:
        print("APROBADO")
    elif tipo_vivienda == "R" and estado_civil == "C" and num_hijos < 2:
        print("APROBADO")
    else:
        print("RECHAZADO")

verificar_aprobacion()