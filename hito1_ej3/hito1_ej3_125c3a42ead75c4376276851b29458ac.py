#Aprobación de créditos
def aprobacion_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion):
    if anios_pertenencia > 10 and num_hijos >=2:
        return "APROBADO"
    elif estado_civil =="C" and num_hijos > 3 and anio_nacimiento >=1970 and anio_nacimiento <=2023:
        return "APROBADO"
    elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
        return "APROBADO"
    elif ingreso > 3500000 and anios_pertenencia > 5:
        return  "APROBADO"
    elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

ingreso = float(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el numero de hijos: "))
anios_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = str(input("Ingrese su estado civil (S soltero, C casado): "))
ubicacion = str(input("Ingrese su ubicacion (U urabano, R rural: "))

resultado = aprobacion_credito(ingreso,anio_nacimiento,num_hijos,anios_pertenencia,estado_civil,ubicacion)
print(resultado)
      