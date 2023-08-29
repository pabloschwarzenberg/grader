def verificar_aprobacion(income, birth_year, num_children, years_at_bank, marital_status, location):
    if years_at_bank > 10 and num_children >= 2:
        return True
    elif marital_status == "C" and num_children > 3 and 45 <= (2023 - birth_year) <= 55:
        return True
    elif income > 2500000 and marital_status == "S" and location == "U":
        return True
    elif income > 3500000 and years_at_bank > 5:
        return True
    elif location == "R" and marital_status == "C" and num_children < 2:
        return True
    else:
        return False

def obtener_datos_cliente():
    income = int(input("Ingrese su ingreso en pesos: "))
    birth_year = int(input("Ingrese su año de nacimiento: "))
    num_children = int(input("Ingrese el número de hijos: "))
    years_at_bank = int(input("Ingrese los años de pertenencia al banco: "))
    marital_status = input("Ingrese su estado civil (S para soltero, C para casado): ")
    location = input("Ingrese si vive en ciudad (U) o campo (R): ")

    return income, birth_year, num_children, years_at_bank, marital_status, location

income, birth_year, num_children, years_at_bank, marital_status, location = obtener_datos_cliente()

if verificar_aprobacion(income, birth_year, num_children, years_at_bank, marital_status, location):
    print("APROBADO")
else:
    print("RECHAZADO")