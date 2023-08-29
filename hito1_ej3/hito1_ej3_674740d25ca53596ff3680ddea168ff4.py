#Aprobación de créditos:
#Definir función y condicionales:
def evaluar():
    ingreso = float(input("Ingrese su ingreso en pesos: "))
    nacimiento = int(input("Ingrese su año de nacimiento: "))
    nHijos = int(input("Ingrese el número de hijos: "))
    pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
    estadoCivil = str(input("Ingrese su estado civil (S para soltero, C para casado): "))
    ubicacion = str(input("Ingrese su ubicación (U para urbano, R para rural): "))

    if (pertenencia > 10) and (nHijos >= 2):
        return "APROBADO"
    elif (estadoCivil == "C") and (nHijos > 3) and (45 <= (2023 - nacimiento) <= 55):
        return "APROBADO"
    elif (ingreso > 2500000) and (estadoCivil == "S") and (ubicacion == "U"):
        return "APROBADO"
    elif (ingreso > 3500000) and (pertenencia > 5):
        return "APROBADO"
    elif (ubicacion == "R") and (estadoCivil == "C") and (nHijos < 2):
        return "APROBADO"
    else:
        return "RECHAZADO"

#Llamar función como resultado:
resultado = evaluar()
print("El resultado de la evaluación del crédito es:", resultado)      