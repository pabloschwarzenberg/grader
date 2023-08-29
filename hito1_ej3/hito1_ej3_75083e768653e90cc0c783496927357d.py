ingreso = int(input("Ingreso: "))
anoNac = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese cantidad de hijos: "))
pert = int(input("Ingrese cantidad de años que pertenece al banco:"))
estadoCivil = input("Ingrese 'S' para Soltero o 'C' para Casado: ")
vive = input("Ingrese 'U' si vive en la ciudad o 'R' si vive en el Campo")


if pert >= 10 and hijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and hijos >= 3 and anoNac < 1973 and anoNac > 1963:
    print("APROBADO")
elif ingreso > 2500000 and estadoCivil == 'S' and vive == 'U':
    print("APROBADO")
elif ingreso > 3500000 and pert >= 5:
    print("APROBADO")
elif vive == 'R' and estadoCivil == 'C' and hijos < 2:
    print("APROBADO")
else:
    print("REPROBADO")