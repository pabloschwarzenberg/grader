ingreso=int(input("Ingresos del cliente"))
nacimiento=int(input("ingresa tu año de nacimiento"))
hijos = int(input("ingrese el numero de hijos"))
tiempocliente=int(input("ingrese los años que pertenece al banco"))
civil = input("ingrese S para soltero o C para casado")
vivienda = input("ingrese donde vive U para urbano, R para Rural")
edad = (2020 - nacimiento)


if tiempocliente > 10 and hijos >=2:
    print("APROBADO")
elif civil == "c"or "C" and hijos > 3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingreso > 2500000 and civil == "s" or "S" and vivienda == "u" or "U":
    print("APROBADO")
elif ingreso > 3500000 and tiempocliente > 5:
    print("APROBADO")
elif vivienda == "r" or "R" and hijos <2 and civil== "c" or "C":
    print("APROBADO")
else:
    print("RECHAZADO")