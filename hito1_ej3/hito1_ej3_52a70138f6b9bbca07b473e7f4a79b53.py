#DATOS
ingreso = int(input("Ingresa cuanto ganas en pesos: "))
edad = int(input("En que año nacio?: "))
hijos = int(input("Ingresa la cantidad de hijos que tienes: "))
años_banco = int(input("¿Hace cuantos años es ud cliente del banco?: "))
estado = input("Ingresa tu estado civil(S para soltero, C para casado): ")
casa = input("Ud vive en un lugar rural o en un lugar urbano?(U para urbano y R para rural): ")
edad = 2021-edad
i = 0
##################################
while (i == 0):
    if (años_banco >= 10 ) and (hijos > 2):
        print("APROBADO")
        i = i + 1
    elif(estado == "C") and (hijos > 3) and ((edad >= 45) and (edad <= 55)):
        print("APROBADO")
        i = i + 1
    elif(ingreso >= 2500000) and (estado == "S") and (casa == "U"):
        print("APROBADO")
        i = i + 1
    elif(ingreso >= 3500000) and (años_banco >= 5):
        print("APROBADO")
        i = i + 1
    elif(casa == "R") and (estado == "C") and (hijos < 2):
        print("APROBADO")
        i = i + 1
    else:
        print("RECHAZADO")
        i = i+1