ingresos = int(input("Ingresa sus ingresos mensuales: "))
edad = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingresa su cantidad de hijos: "))
años_banco = int(input("Ingrese la cantidad de años perteneciente al banco: "))
estado = input("Ingresa si esta casado(C) o soltero(S): ")
casa = input("Ingrese si vive en Campo (C) o en ciudad(U)): ")
edad = 2021-edad
i = 0

while (i == 0):
    if (años_banco >= 10 ) and (hijos > 2):
        print("A SIDO APROBADO")
        i = i + 1
    elif(estado == "C") and (hijos > 3) and ((edad >= 45) and (edad <= 55)):
        print("A SIDO APROBADO")
        i = i + 1
    elif(ingresos >= 2500000) and (estado == "S") and (casa == "U"):
        print("A SIDO APROBADO")
        i = i + 1
    elif(ingresos >= 3500000) and (años_banco >= 5):
        print("A SIDO APROBADO")
        i = i + 1
    elif(casa == "R") and (estado == "C") and (hijos < 2):
        print("A SIDO APROBADO")
        i = i + 1
    else:
        print("A SIDO RECHAZADO")
        i = i+1      