#Aprobación de créditos
hijos = int(input("Ingrese número de hijos "))
ingreso = int(input("Ingrese su sueldo en pesos "))
anonacimiento = int(input("ingrese año de nacimiento "))
pertenencia = int(input("ingrese años de pertenencia al banco "))
estadocivil = input("Ingrese una S si es que está soltero y una C si es que está casado ")
vive = input("Ingrese una U si es que vive en zona urbana y una R si es que vive en zona rural ")

edad = 2023 - anonacimiento

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estadocivil == "C" and hijos > 3 and 45 > edad >55:
    print("APROBADO")
elif ingreso > 2500000 and estadocivil == "S" and vive == "U":
    print("APROBADO")
elif ingreso > 35000000 and pertenencia > 5:
    print("APROBADO")
elif vive == "R" and estadocivil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")    