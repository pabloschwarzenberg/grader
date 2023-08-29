ingreso = int(input("ingrese su sueldo: "))
año = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese cuantos hijos tienes: "))
banco = int(input("ingrese años de pertenencia al banco"))
estadocivil = str(input("esta casado: C o soltero: S"))
vive = str(input("Urbano : U o Rural: R"))

año = 2021 - año
str("C")
str("S")
if banco > 10 and hijos > 1:
    print("APROBADO")
    
elif estadocivil == "C" and hijos > 3 and año > 44 and año < 56:
    print("APROBADO")
    
elif ingreso > 2500000 and estadocivil == "S" and vive == "U":
    print("APROBADO")

elif ingreso > 3500000 and banco > 5:
    print("APROBADO")
elif vive == "R" and estadocivil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      