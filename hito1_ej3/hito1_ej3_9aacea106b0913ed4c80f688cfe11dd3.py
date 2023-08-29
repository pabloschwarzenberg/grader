def verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, tipo_residencia):
    if anos_banco > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and tipo_residencia == "U":
        return True
    elif ingreso > 3500000 and anos_banco > 5:
        return True
    elif tipo_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

# Solicitar datos al cliente
ingreso = float(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
tipo_residencia = input("Ingrese el tipo de residencia (U para urbano, R para rural): ")

# Verificar aprobación
aprobado = verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, tipo_residencia)

# Imprimir resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")