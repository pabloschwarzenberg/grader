#Aprobación de créditos
ingreso = int(input("Ingreso(en pesos): "))
año = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese numero de hijos: "))
año_banco = int(input("Años de pertenencia al banco: "))
estado_civil = str(input("Ingrese estado civil , S : soltero , C :casado: "))
vive_en = str(input("¿Vive en campo o ciudad?, U : urbano, R: rural: "))

if año_banco > 10 and hijos >= 2:
    print("APROBADO")
if str(estado_civil) == "c" and hijos > 3 and año < 1976 and año > 1966:
    print("APROBADO")
if ingreso > 2500000 and str(estado_civil) == "s" and str(vive_en) == "u":
    print("APROBADO")
if ingreso > 3500000 and año_banco > 5:
    print("APROBADO")
if str(vive_en) == "R" and  str(estado_civil) == "C" and hijos < 2:
    print("APROBADO")


