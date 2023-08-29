#Aprobación de créditos
Ingresos = eval(input("Ingrese el valor de sus ingresos: "))
año_nacimineto = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese numero de hijos: "))
años_banco = int(input("cuantos años lleva en el banco: "))
estado_civil = input("Si usted es casado o casada, ingrese la letra C, si usted es soltero o soltera, ingrese la letra S: ")
campo_ciudad = input("Si vive en un campo ingrese la letra R, si vive en ciudad U: ")

if ((años_banco > 10) and (hijos >= 2)):
    print("APROBADO")
elif ((estado_civil == "C") and (hijos > 3) and (año_nacimiento <= 1975) and (año_nacimiento >= 1966)):
    print("APROBADO")
elif((Ingresos > 2500000) and (estado_civil == "S") (campo_ciudad == "U")):
    print("APROBADO")
elif((Ingresos > 3500000) and (años_banco > 5)):
    print("APROBADO")
elif((campo_ciudad == "R") and (hijos < 2)):
    print("APROBADO")
else:
    print("RECHAZADO")

              