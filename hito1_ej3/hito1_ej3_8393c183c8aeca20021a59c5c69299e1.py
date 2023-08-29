#Aprobación de créditos
ingreso = int(input("Escriba sus ingresos en pesos: "))
anonacimiento = int(input("¿Cuál es su año de nacimiento? "))
hijos = int(input("¿Cuántos hijos tiene? "))
anospertenencia = eval(input("¿Cuántos años ha pertenecido al banco? "))
estadocivil = input("Ingrese su estado civil poniendo S si está soltero o C si está casado: ")
vivienda = input("Escriba U si vive en un lugar urbano, o R si el lugar es rural: ")

if (anospertenencia > 10) or (hijos >= 2):
    print("APROBADO")

elif (estadocivil == "C") or (hijos > 3) or (anonacimiento >= 1966 and anonacimiento <= 1976):
    print("APROBADO")

elif (ingreso > 2500000) or (estadocivil == "S") or (vivienda == "C"):
    print("APROBADO")

elif (ingreso > 3500000) or (anospertenencia > 5):
    print("APROBADO")

elif (vivienda == "C") or (estadocivil == "C") or (hijos < 2):
    print("APROBADO")

else:
    print("RECHAZADO")      