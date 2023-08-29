def verificar_aprobacion_credito():
    ingreso = float(input("Ingrese su ingreso en pesos: "))
    ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
    num_hijos = int(input("Ingrese el numero de hijos: "))
    anos_de_pertenencia_banco = int(input("Ingrese los años de pertenencia al banco: "))
    estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
    ubicacion = input("Ingrese su ubicacion (U para urbano, R para rural): ")
     
    if anos_de_pertenencia_banco > 10 and num_hijos >= 2:
        print("APROBADO")
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        print("APROBADO")
    elif ingreso > 250000 and estado_civil == "S" and ubicacion == "U":
        print("APROBADO")
    elif ingreso > 350000 and anos_de_pertenencia_banco > 5:
        print("APROBADO")
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        print("APROBADO")
    else:
        print("RECHAZADO")

verificar_aprobacion_credito()