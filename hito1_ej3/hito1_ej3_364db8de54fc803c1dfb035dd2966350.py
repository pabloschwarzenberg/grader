#Aprobación de créditos
print("Atencion Automizada De Creditos De Consumo")
print("Complete los campos con los datos solicitados")
ingreso = int(input("Favor indique su nivel de ingresos: "))
año_de_nacimiento = int(input("Favor indique su año de nacimiento: "))
edad = suma = año_de_nacimiento - 2021
numero_de_hijos = int(input("Indique la cantidad de hijos que usted tiene: "))
Años_en_el_banco = int(input("¿Hace cuantos años pertenece al banco?: "))
Estado_civil = print("Indique su Estado Civil segun las opciones con Mayuscula")
while True:
    print("S-Soltero")
    print("C-Casado")
    opcion = input("Opcion: ")
    if opcion == "S":
        Estado_civil = "Soltero"
        break
    if opcion == "C":
        Estado_civil = "Casado"
        break
    else:
        print("ingrese una opcion valida")
while True:
    Campo_Ciudad = print("Indique si vive en campo o ciudad con Mayuscula")
    print("R-Rural")
    print("U-urbano")
    Opcion = input("Opcion: ")
    if Opcion == "R":
        Campo_Ciudad = "Rural"
        break
    elif Opcion == "U":
        Campo_Ciudad = "Urbano"
        break
    else:
        print("ingrese una opcion valida")
print("Calculando su solicitud")
if Años_en_el_banco >= 10 and numero_de_hijos >= 2:
    print("APROBADO")
elif Estado_civil == "Casado" and numero_de_hijos >= 3 and edad:
    print("APROBADO")
elif ingreso >= 2500000 and Estado_civil == "Soltero" and Campo_Ciudad == "Urbano":
    print("APROBADO")
elif ingreso >= 3500000 and Años_en_el_banco >= 5:
    print("APROBADO")
elif Campo_Ciudad == "Rural" and Estado_civil == "Casado" and numero_de_hijos <=2:
    print("APROBADO")
else:
    print("RECHAZADO")