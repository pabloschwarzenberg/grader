#Aprobación de créditos
m = int(input("Ingresos: $"))
an = int(input("Ingrese año de nacimiento: "))
nh = int(input("Ingrese número de hijos: "))
ab = int(input("Ingrese años de pertenencia al banco: "))
ec = str(input("Ingrese estado civil(S: soltero, C: casado): "))
u = str(input("vive en campo o cuidad (U: urbano, R: rural): "))

edad = (2022-an)

if (ec == "S" or ec == "C") and (u == "U" or u == "R"):
    if ab > 10 and nh >= 2:
        print("APROBADO")
    elif ec == "C" and nh > 3 and (edad >= 45 and edad <=55):
        print("APROBADO")
    elif m > 2500000 and ec == "S" and u =="U":
        print("APROBADO")
    elif m > 3500000 and ab > 5:
        print("APROBADO")
    elif u == "R" and ec == "C" and nh < 2:
        print("APROBADO")
    else:
        print("RECHASADO")
else:
    print("Error, intentelo de nuevo")     