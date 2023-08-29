def evaluar_credito():
    ingreso = int(input("Ingrese su ingreso en pesos: "))
    ano = int(input("Ingrese su anio de nacimiento: "))
    n_hijos = int(input("Ingrese su numero de hijos: "))
    anobanco = int(input("Ingrese sus anos pertenecientes al banco: "))
    estadocivil = input("Ingrese su estado civil (Soltero = S)(Casado = C): ")
    residencia = input("Ingrese su Residencia (U = Urbano) (R = rural): ")
    aprobacion = False

    if anobanco >= 10 and n_hijos >= 2:
        aprobacion = True
    elif estadocivil == "C" and n_hijos > 3 and 45 <= (2023 - ano) <= 55:
        aprobacion = True
    elif ingreso > 2500000 and estadocivil == "S" and residencia == "U":
        aprobacion = True
    elif ingreso > 3500000 and anobanco > 5:
        aprobacion = True
    elif residencia == "R" and estadocivil == "C" and n_hijos < 2:
        aprobacion = True
    if aprobacion:
        print("APROBADO")
    else:
        print("RECHAZADO")

evaluar_credito()
