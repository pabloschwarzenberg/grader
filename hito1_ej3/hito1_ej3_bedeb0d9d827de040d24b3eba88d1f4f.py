#Aprobación de créditos
from datetime import date

ingresoPesos = eval(input("Escriba su ingreso en pesos: "))
anoNacimiento = int(input("ingrese su año de nacimiento: "))
numHijos = int(input("Ingrese la cantidad de hijos: "))
afiliacionBanco = int(input("ingrese la cantidad de años de afiliación al banco: "))
estadoCivil = input("seleccione su estado civil ('S'=soltero / 'C'= casado ): ")
tipoLocalidad = input("seleccione si vive en campo o ciudad ('U'=urbano / 'R' = rural)")

fechaActual = date.today()
anoActual = fechaActual.year

# print('añoNacimiento', añoNacimiento, 'añoActual',añoActual)

edadActual = anoActual - anoNacimiento
# print(edadActual)


if afiliacionBanco > 10 and numHijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and numHijos > 3 and (45 <= edadActual <= 55):
    print("APROBADO")
elif ingresoPesos > 2500000 and estadoCivil == "S" and tipoLocalidad == "U":
    print("APROBADO")
elif ingresoPesos > 3500000 and afiliacionBanco > 5:
    print("APROBADO")
elif tipoLocalidad == "R" and estadoCivil == "C" and numHijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
