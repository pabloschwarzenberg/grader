#Aprobación de créditos

print("debe ingresar los siguientes datos personales")
ingresos = int(input("ingresos: $"))
nacimiento = int(input("año de nacimiento: "))
hijos = int(input("numero de hijos: "))
pertenencia = int(input("años de pertenencia al banco: "))
estado = input("estado civil(S:soltero, C:casado): ")
vive = input("lugar donde vive(U: urbano, R: rural: ")


if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
else:
    print("NO APROBADO")
if estado == "C" and hijos > 3 and 1975 < nacimiento < 1965:
    print("APROBADO")
else:
    print("NO APROBADO")
if ingresos > 2500000 and estado == "S" and estado == "s" and vive == "R" and vive == "r":
    print("APROBADO")
else:
    print("NO APROBADO")
if ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")
else:
    print("NO APROBADO")
if vive == "r" and vive == "R" and estado == "C" and estado == "c" and hijos < 2:
    print("APROBADO")
else:
    print("NO APROBADO")