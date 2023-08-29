def aprobar_credito(ingreso, nacimiento, hijos, pertenencia, estado_civil, ubicacion):
    """
    Función para determinar si se aprueba un crédito de consumo según las reglas establecidas por el banco.

    Argumentos:
    - ingreso: entero representando el ingreso del cliente en pesos
    - nacimiento: entero representando el año de nacimiento del cliente
    - hijos: entero representando el número de hijos del cliente
    - pertenencia: entero representando los años de pertenencia del cliente al banco
    - estado_civil: string representando el estado civil del cliente ("S" para soltero, "C" para casado)
    - ubicacion: string representando la ubicación del cliente ("U" para urbano, "R" para rural)

    Retorna:
    - resultado: string indicando si el crédito está "APROBADO" o "RECHAZADO"
    """
    if pertenencia > 10 and hijos >= 2:
        resultado = "APROBADO"
    elif estado_civil == "C" and hijos > 3 and nacimiento >= 45 and nacimiento <= 55:
        resultado = "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        resultado = "APROBADO"
    elif ingreso > 3500000 and pertenencia > 5:
        resultado = "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and hijos < 2:
        resultado = "APROBADO"
    else:
        resultado = "RECHAZADO"

    return resultado

# Solicitar los datos al cliente
ingreso = int(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

# Determinar si se aprueba o rechaza el crédito
resultado = aprobar_credito(ingreso, nacimiento, hijos, pertenencia, estado_civil, ubicacion)

# Mostrar el resultado
print("Resultado:", resultado)

      