#Aprobación de créditos
pesos = int(input("Ingrese sus ingresos en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos que tiene: "))
banco = int(input("Ingrese la cantidad de años de pertenencia al banco: "))
civil = input("Ingrese su estado civil *Ingrese 'S' si está soltero e ingrese 'C' si está casado.*: ")
lugar = input("Ingrese el lugar donde vive *Ingrese 'U' si vive en una zona urbana o 'R' si vive en una zona rural*: ")
a = 2022 - nacimiento
if banco > 10 and hijos >= 2:
    print("APROBADO")
elif civil == "C" and hijos > 3 and a > 44 and a < 56:
    print("APROBADO")
elif pesos > 2500000 and civil == "S" and lugar == "U":
    print("APROBADO")
elif pesos > 3500000 and banco > 5:
    print("APROBADO")
elif lugar == "R" and civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")   