def verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, lugar_residencia):
    if anos_banco > 10 and num_hijos >= 2:
        return True
    elif estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
        return True
    elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return True
    elif ingreso > 3500000 and anos_banco > 5:
        return True
    elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return True
    else:
        return False

# Solicitar al cliente los datos necesarios
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese el lugar de residencia (U para urbano, R para rural): ")

# Verificar la aprobación del crédito
aprobado = verificar_aprobacion(ingreso, ano_nacimiento, num_hijos, anos_banco, estado_civil, lugar_residencia)

# Imprimir el resultado
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
      