#Aprobación de créditos
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
nacimiento = int(input("Ingrese el anio de nacimiento: "))
hijos = int(input("Ingrese el numero de hijos: "))
pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil : ")
ubicacion = input("Ingrese la ubicación : ")



if pertenencia > 10 and hijos >= 2:
    aprobado = True
elif estado_civil == "C" and hijos > 3 and nacimiento >= 1968 and nacimiento <= 1978:
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    aprobado = True
elif ingreso > 3500000 and pertenencia > 5:
    aprobado = True
elif ubicacion == "R" and estado_civil == "C" and hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")