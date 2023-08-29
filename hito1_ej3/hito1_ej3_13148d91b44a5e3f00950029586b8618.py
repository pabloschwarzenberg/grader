#Aprobación de créditos
 def verificar_aprobacion(ingreso, año_nacimiento, num_hijos, años_pertenencia, estado_civil, ubicacion):
    if años_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and año_nacimiento >= 45 and año_nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and años_pertenencia > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Solicitar los datos al cliente
ingreso_cliente = float(input("Ingrese su ingreso mensual en pesos: "))
año_nacimiento_cliente = int(input("Ingrese su año de nacimiento: "))
num_hijos_cliente = int(input("Ingrese el número de hijos que tiene: "))
años_pertenencia_cliente = int(input("Ingrese los años que ha pertenecido al banco: "))
estado_civil_cliente = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion_cliente = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Verificar la aprobación del crédito
resultado = verificar_aprobacion(ingreso_cliente, año_nacimiento_cliente, num_hijos_cliente, años_pertenencia_cliente, estado_civil_cliente, ubicacion_cliente)

# Mostrar el resultado
print("Estado de aprobación del crédito: ", resultado)

Ingrese su ingreso mensual en pesos: 2800000
Ingrese su año de nacimiento: 1970
Ingrese el número de hijos que tiene: 4
Ingrese los años que ha pertenecido al banco: 12
Ingrese su estado civil (S para soltero, C para casado): C
Ingrese su ubicación (U para urbano, R para rural): U
Estado de aprobación del crédito:  APROBADO




     