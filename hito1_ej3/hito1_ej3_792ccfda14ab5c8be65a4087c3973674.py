dato_1 = int(input("Indique su ingreso: "))
dato_2 = int(input("Ingrese su año de nacimiento: "))
dato_3 = int(input("Ingrese su número de hijos: "))
dato_4 = int(input("Ingrese sus años de permanencia en el banco: "))
dato_5 = str(input("Ingrese su estado civil: "))
dato_6 = str(input("Indique si vive en campo o ciudad: "))

if dato_4 > 10:
    if dato_3 >= 2:
        print("APROBADO")
if dato_3 > 3:
    if dato_2 >= 1965:
        if dato_2 <= 2010:
            print("APROBADO")
if dato_1 > 2500000:
    if dato_5 == "S":
        if dato_6 == "U":
            print("APROBADO")
if dato_1 > 3500000:
    if dato_4 > 5:
        print("APROBADO")
if dato_6 == "R":
    if dato_5 == "C":
        if dato_3 < 2:
            print("APROBADO")
else:
    print("RECHAZADO")