def verificar_aprobacion(ingreso, año_nacimiento, num_hijos, años_banco, estado_civil, lugar_residencia):
    if años_banco > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and año_nacimiento >= 45 and año_nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
        return "APROBADO"
    elif ingreso > 3500000 and años_banco > 5:
        return "APROBADO"
    elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Solicitar información al cliente
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
año_nacimiento = int(input("Ingrese el año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
años_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese el lugar de residencia (U para urbano, R para rural): ")

# Verificar la aprobación del crédito
resultado = verificar_aprobacion(ingreso, año_nacimiento, num_hijos, años_banco, estado_civil, lugar_residencia)

# Imprimir el resultado
print("Resultado:", resultado)
      