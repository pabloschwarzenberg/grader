#Aprobación de créditos
ingreso = int(input("introduzaca su ingreso: "))
año = int(input("Ingrese año de nacimiento: "))
numHijos = int(input("Ingrese número de hijos: "))
añosPertenencia = int(input("Ingrese cantidad de años cliente del banco: "))
estadoCivil = input("Ingrese estado civil(S: soltero)o(C: casado): ")
vive = input("Ingrese sector donde vive (U: urbano)o (R:rural): ")

if añosPertenencia > 10 and numHijos >= 2:
    print("APROBADO. ")
elif estadoCivil == "C" and numHijos > 3 and  1965 <= ano <= 1975:
    print("APROBADO. ")
elif ingreso > 2500000 and estadoCivil == "S" and vive == "U":
    print("APROBADO. ")
elif ingreso > 3500000 and añosPertenencia > 5:
    print("APROBADO. ")
elif vive == "R" and estadoCivil == "C" and numHijos < 2:
    print("APROBADO. ")
else:
    print("RECHAZADO. ")

      