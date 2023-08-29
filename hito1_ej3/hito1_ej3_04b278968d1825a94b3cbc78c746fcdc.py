#Entrada
ingreso = (int(input("Ingreso:")))
nacimiento = int(input("Año de nacimiento:"))
hijos = (int(input("ingrese número de hijos: ")))
años_de_antiguedad = int(input("Años de pertenencia al banco:"))
estado_civil = input("Estado civil si es soltero S , si es casado C:")
lugar = input("Si vive en campo R, o ciudad U:")
edad = (2021 - nacimiento)

 #Procesamiento
if años_de_antiguedad >= 11 and hijos >= 2:
    print("APROBADO")
else:
    print ("RECHAZADO")
    if(3 < hijos and 45 <= edad <= 55 and 3 < hijos
    and (estado_civil == "C")):
        print("APROBADO")
    else: print("RECHAZADO")
    if 2500000 < ingreso and (estado_civil == "S") and lugar == "U":
        print("APROBADO")
    if 3500000 < ingreso and años_de_antiguedad > 5:
        print("APROBADO")
    else:
        ("RECHAZADO")
    if lugar == "R" and estado_civil == "C" and hijos <= 1:
        print("APROBADO")
    else:
        print("RECHAZADO")


