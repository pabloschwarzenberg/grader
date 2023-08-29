#Aprobación de créditos
var_Ingreso = int(input("Ingrese el monto de sus ingresos: "))
var_AnoNacimiento = int(input("Ingrese el año en el que nació: "))
var_NumHijos = int(input("¿Cuantos hijos tiene?: "))
var_Antiguedad = int(input("¿Cuantos años de antigüedad tiene con el banco?: "))
var_EstadoCivil = input("S: Soltero, C: Casado.")
var_DondeVive = input("U: Urbano, R: Rural.")
var_AnoActual = 2021
var_Edad = 2021 - var_AnoNacimiento
if (var_Antiguedad >= 10 and var_NumHijos >= 2):
    print("APROBADO")
elif (var_EstadoCivil == "C" and var_NumHijos > 3 and (var_Edad >= 45 and var_Edad <= 55)):
    print("APROBADO")
elif (var_Ingreso > 2500000 and var_EstadoCivil == "S" and var_DondeVive == "U"):
    print("APROBADO")
elif (var_Ingreso > 3500000 and var_Antiguedad > 5):
    print("APROBADO")
elif (var_DondeVive == "R" and var_EstadoCivil == "C" and var_NumHijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")