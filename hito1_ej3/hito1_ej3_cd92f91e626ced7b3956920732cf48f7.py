#Aprobación de créditos
def evaluar_credito(ingreso, nacimiento, hijos, anios_pertenencia, estado_civil, ubicacion):
    if anios_pertenencia > 10 and hijos >= 2:
        return "APROBADO"
    elif estado_civil == "C" and hijos > 3 and nacimiento >= 45 and nacimiento <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anios_pertenencia > 5:
        return "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"


# Solicitar al cliente que ingrese su información
ingreso = int(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
ubicacion = input("Ingrese su ubicación (U: urbano, R: rural): ")

# Evaluar la aprobación del crédito
resultado = evaluar_credito(ingreso, nacimiento, hijos, anios_pertenencia, estado_civil, ubicacion)

# Imprimir el resultado
print("Resultado:", resultado)
