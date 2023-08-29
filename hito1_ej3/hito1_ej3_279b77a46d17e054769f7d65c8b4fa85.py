#Aprobación de créditos
ingreso = int(input("ingrese ingreso: "))
nacimiento = int(input("ingrese año de nacimiento: "))
hijos = int(input("ingrese numero de hijos: "))
años = int(input("ingrese años de pertenencia al banco: "))
estado = input("ingrese soltero o casado : ")
vivienda = input("donde vive? ")
edad = 2023 - nacimiento 
if años > 10 and hijos >= 2:
    print("APROBADO")
if estado == "C" and hijos > 3 and 45<edad<55:
    print("APROBADO")
if ingreso > 2500000 and estado == "S" and vivienda == "U":
    print("APROBADO")
if ingreso > 3500000 and años > 5:
    print("APROBADO")
if vivienda == "R" and estado =="C" and hijos <2 :
    print("APROBADO")