#Aprobación de créditos
ingreso = int(input("Ingreso: (en pesos) "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
años = int(input("Años de pertenecia al banco: "))
estado_civil = str(input("S: soltero o C: casado "))
campo_ciudad= str(input("R : rural o U : urbano "))

if años > 10 and hijos >= 2:
    print("APROBADO")
if estado_civil == "C" and hijos > 3 and 45 > años < 55 :
    print("APROBADO")
if ingreso > 2500000 and estado_civil == "S" and campo_ciudad == "U":
    print("APROBADO")
if ingreso > 3500000 and años > 5:
    print("APROBADO")
if campo_ciudad == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")