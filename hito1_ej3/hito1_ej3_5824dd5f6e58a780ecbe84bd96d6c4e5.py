#Aprobación de créditos
ingreso = float(input("digite el ingreso en pesos: "))
año = int(input("Ingrese el año: "))
nhijos= int(input("Ingrese el numero de hijos: "))
banco = int(input("Ingrese años de pertenencia al banco: "))
ec= input("Ingrese S para soltero y C para casado: ")
localidad= input("Ingrese U para urbano y R para rural")

if banco >10:
    print("APROBADO")
elif ec == "C" and nhijos >3 and año >= 45 and año <=55:
    print("APROBADO")
elif ingreso > 2500000 and ec == "S" and banco >5 and localidad == "U":
    print("Aprobado")
elif ingreso > 3500000 and banco >5:
    print("Aprobado")
elif ec == "C" and localidad =="R" and nhijos <2:
    print("Aprobado")
else:
    print("RECHAZADO")        