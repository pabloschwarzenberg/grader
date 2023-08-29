#Aprobación de créditos
def aprobar_credito():
    # Solicitar al cliente la información requerida
    ingreso = float(input("Ingrese su ingreso en pesos: "))
    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el número de hijos: "))
    anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

    # Verificar las reglas para aprobar el crédito
    if anos_pertenencia > 10 and num_hijos >= 2:
        print("APROBADO")
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        print("APROBADO")
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        print("APROBADO")
    elif ingreso > 3500000 and anos_pertenencia > 5:
        print("APROBADO")
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        print("APROBADO")
    else:
        print("RECHAZADO")

# Llamar a la función para aprobar el crédito
aprobar_credito()
      