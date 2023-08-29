def aprobar_credito(ingreso, año_nacimiento, num_hijos, años_banco, estado_civil, ubicacion):
    if años_banco > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and año_nacimiento >= 45 and año_nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and años_banco > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Ejemplo de uso
ingreso_cliente = float(input("Ingrese el ingreso del cliente (en pesos): "))
año_nacimiento_cliente = int(input("Ingrese el año de nacimiento del cliente: "))
num_hijos_cliente = int(input("Ingrese el número de hijos del cliente: "))
años_banco_cliente = int(input("Ingrese los años de pertenencia al banco del cliente: "))
estado_civil_cliente = input("Ingrese el estado civil del cliente ('S' para soltero, 'C' para casado): ")
ubicacion_cliente = input("Ingrese la ubicación del cliente ('U' para urbano, 'R' para rural): ")

resultado = aprobar_credito(ingreso_cliente, año_nacimiento_cliente, num_hijos_cliente, años_banco_cliente, estado_civil_cliente, ubicacion_cliente)
print("Resultado:", resultado)
      