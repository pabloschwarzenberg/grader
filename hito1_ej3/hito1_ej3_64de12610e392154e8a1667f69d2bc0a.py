#Aprobación de créditos
Ingreso = int(input("Ingrese sus ingresos en pesos: "))
Nacimiento = int(input("Ingrese su año de nacimiento: "))
Hijos = int(input("Ingrese la cantidad de hijos que tiene: "))
Pertenencia = int(input("Ingrese cuantos años de pertenencia al banco tiene: "))
Estado = str(input("Ingrese su estado civil, S para soltero, C para casado: "))
Vivienda = str(input("Ingrese donde vive, U para urbano, R para rural: "))

#Procedimiento
if Pertenencia > 10 and Hijos >= 2:
    print("APROBADO")
elif Estado == "C" and Hijos > 3 and 2021 - Nacimiento >= 45 and 2021 - Nacimiento <= 55:
    print("APROBADO")
elif Ingreso > 2500000 and Estado == "S" and Vivienda == "U":
    print("APROBADO")
elif Ingreso > 3500000 and Pertenencia > 5:
    print("APROBADO")
elif Vivienda == "R" and Estado == "C" and Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")

#Final
print("Gracias por preferir este banco")