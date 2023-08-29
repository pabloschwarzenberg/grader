# Ejercicio banco
ingreso_pesos = int(input("Introduzca ingreso salarial: "))
nacimiento_ano = int(input("Introduzca el año en el que nacio: "))
hijos = int(input("¿cuantos hijos tiene?: "))
APB = int(input("¿cuantos años de pertenencia tienes en el banco?: "))
ES = str(input("Indique su estado civil (C = CASADO - S = SOLTERO): "))
ciudad = str(input("Indique si vive en el campo o en una ciudad (U = URBANO - R = RURAL): "))
if APB > 10 and hijos > 2:
    print("APROBADO")
else:
    print("RECHAZADO")
if ES == "C" and hijos > 3 and 45 <= nacimiento_ano <= 55:
    print("APROBADO")
else:
    print("RECHAZADO")
if ingreso_pesos > 2500000 and ES == "S" and ciudad == "U":
    print ("APROBADO")
else:
    print("RECHAZADO")
if ingreso_pesos > 3500000 and APB > 5:
    print("APROBADO")
else:
    print("RECHAZADO")
if ciudad =="R" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")