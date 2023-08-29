#Aprobación de créditos
 def evaluar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion):
    if anios_pertenencia > 10 and num_hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 45 and anio_nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anios_pertenencia > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

# Solicitar datos al cliente
ingreso_cliente = int(input("Ingrese el ingreso en pesos: "))
anio_nacimiento_cliente = int(input("Ingrese el año de nacimiento: "))
num_hijos_cliente = int(input("Ingrese el número de hijos: "))
anios_pertenencia_cliente = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil_cliente = input("Ingrese el estado civil (S para soltero, C para casado): ")
ubicacion_cliente = input("Ingrese la ubicación (U para urbano, R para rural): ")

# Llamar a la función y mostrar el resultado
resultado = evaluar_credito(ingreso_cliente, anio_nacimiento_cliente, num_hijos_cliente, anios_pertenencia_cliente, estado_civil_cliente, ubicacion_cliente)
print("El crédito ha sido:", resultado)
