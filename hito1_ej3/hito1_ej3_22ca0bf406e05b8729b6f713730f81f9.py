#Aprobación de créditos

ingreso = float(input("sus ingresos (en pesos): "))
nacimiento = int(input("año de nacimiento: "))
hijos = int(input("numero de hijos: "))
añosBanco = int(input("años de pertenencia al banco: "))
print("S:SOLTERO/C:CASADO")
estadoCivil = input("estado civil S/C: ")
print("U:URBANO/R:RURAL")
lugar = input("si vive en U/R: ")


if añosBanco > 10 and hijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso > 2500000  and estadoCivil == "S" and lugar == "U":
    print("APROBADO")
elif ingreso > 3500000  and añosBanco > 5:
    print("APROBADO")
elif lugar == "R" and hijos <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")     