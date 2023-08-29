import datetime as dT

ingreso = int(input("ingrese ingresos:"))
nacimiento = int(input("ingrese año de nacimiento:"))
nHijos = int(input("Cuantos hijos tiene?:"))
perBanco = int(input("Cuantos años ha estado en el banco?"))
estadoCivil = str(input("Su estado civil?(S = Soltero, C = Casado)"))
lugar = str(input("ingrese sdonde vive(R = Rural, U = Urbano)"))

ahora = dT.datetime.now()
edad = ahora.year - nacimiento



if perBanco > 10 and nHijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and nHijos >= 3 and edad >=45 or edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estadoCivil == "S" and lugar == "U":
    print("APROBADO")
elif ingreso > 3500000 and perBanco > 5:
    print("APROBADO")
elif lugar == "R" and estadoCivil == "C" and nHijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")

