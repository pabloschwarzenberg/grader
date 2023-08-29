#Aprobación de créditos
ingreso = int(input("ingrese ingreso: "))
fecha = int(input("ingrese año de nacimiento: "))
hijos = int(input("ingrese numero de hijos: "))
banco = int(input("cuantos años lleva en el banco: "))
estado_civil = input("ingrese una s si es soltero o c si es casado: ")
provincia = input("ingrese una u por urbano r por rural: ")

edad = 2020 - fecha


if ingreso >= 250000:
    print("APROBADO")

elif (banco > 10 and hijos >= 2
    ) or (estado_civil == "c" or estado_civil == "C" and hijos >= 3
    and edad >= 45 and edad <=55) or (ingreso > 250000
    and estado_civil == "s" or estado_civil == "S" and
    provincia == "u" or provincia == "U") or (ingreso > 350000 and
    banco > 5) or (provincia == "r" or provincia == "R" and
    estado_civil == "c" or estado_civil == "C" and hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")


