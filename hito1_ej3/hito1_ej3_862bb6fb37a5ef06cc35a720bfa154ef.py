#Aprobación de créditos
Ingreso = int(input("Ingrese sus ingresos en pesos:   "))
Año_nacimiento = int(input("Ingrese año de nacimiento:   "))
Numero_de_hijos = int(input("Ingrese numero de hijos:   "))
Años_de_pertenencia_al_banco = int(input("Ingrese número de años de pertenencia al banco:   "))
Estado_civil = input("Ingrese estado civil, C si es casado o S si es soltero:   ")
Ubicacion_domicilio = input ("Ingrese la locación de su domicilio, U si es urbano o R si es rural:   ")

# Procedimiento
edad = 2021 - Año_nacimiento
if Años_de_pertenencia_al_banco >= 10 and Numero_de_hijos >= 2:
    print("APROBADO")
elif Estado_civil is "C":
    if Numero_de_hijos > 3 and 45 <= edad <= 55:
        print("APROBADO")
    elif Numero_de_hijos < 2 and Ubicacion_domicilio is "R":
        print("APROBADO")
elif Ingreso > 2500000:
    if Estado_civil is "S" and Ubicacion_domicilio is "U":
        print("APROBADO")
    elif Ingreso > 3500000 and Años_de_pertenencia_al_banco > 5:
        print("APROBADO")
else:
    print("RECHAZADO")