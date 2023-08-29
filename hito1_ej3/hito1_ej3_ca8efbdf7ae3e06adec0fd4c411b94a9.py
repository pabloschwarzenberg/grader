#Aprobación de créditos

from datetime import datetime

ingreso = int(input("Ingrese su sueldo en pesos:  "))
añoDeNacimiento = int(input("Ingrese su año de nacimiento:  "))
numeroDeHijos = int(input("Ingrese numero de hijos:  "))
añoDeAntiguedadBanco = int(input("Ingrese cuantos años de pertenencia al banco lleva:  "))
estadoCivil = input("Ingrese S si te encuentras soltero, Ingresa C si te encuentras casado:  ")
campoCiudad = input("selecciona U si vive en ciudad o R si vive en el campo:  ")

soltero = "S"
casado = "C"

urbano = "U"
rural = "R"

hoy = datetime.now()
hoy = int(hoy.strftime('%y%m%d'))

hoy = str(hoy)
len(hoy)

hoy = hoy[:2]
añoActual = int(hoy) + 2000

edad = añoActual - añoDeNacimiento
print(edad)


if estadoCivil == "S":
    estadoCivil = "S"
else:
    estadoCivil = "C"

if campoCiudad == "U":
    campoCiudad = "U"
else:
    campoCiudad = "R"

if numeroDeHijos >= 2 and añoDeAntiguedadBanco > 10:
    print("APROBADO 1")
elif estadoCivil == "C" and numeroDeHijos > 3 and edad in range(45, 55):
    print("APROBADO 2")
elif ingreso > 2500000 and estadoCivil == "S" and campoCiudad == "U":
    print("APROBADO 3")
elif ingreso > 3500000 and añoDeAntiguedadBanco > 5:
    print("APROBADO 4")
elif campoCiudad == "R" and estadoCivil == "C" and numeroDeHijos < 2:
    print("APROBADO 5")
else:
    print("RECHAZADO")
    