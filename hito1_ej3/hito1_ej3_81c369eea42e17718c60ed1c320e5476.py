#Aprobación de créditos
ingreso = int(input("Dinero a ingresar (en pesos): "))
ano = int(input("Año de nacimiento: "))
n_hijos = int(input("Ingrese cuantos hijos tiene: "))
anos = int(input("Años a los que pertenence al banco: "))
estado_civil = input("Ingrese estado civil (C = casado, S = Soltero): ")
ubicacion = input("Ingrese si vive en campo o ciudad (U = ciudad, R = campo): ")
edad = 2021 - ano

if (anos > 10) and (n_hijos >= 2):
    print("APROBADO")
elif (estado_civil == "C") and (n_hijos > 3) and ((edad >= 45) and (edad <= 55)):
    print("APROBADO")
elif (ingreso > 2500000) and (estado_civil == "S") and (ubicacion == "U"):
    print("APROBADO")
elif (ingreso > 3500000) and (anos > 5):
    print("APROBADO")
elif (ubicacion == "R") and (estado_civil == "C") and (n_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
