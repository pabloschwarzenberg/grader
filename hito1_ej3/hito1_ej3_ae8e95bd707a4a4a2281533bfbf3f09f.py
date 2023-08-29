ingreso = int(input("ingrese su ingresos: "))
año_nacimiento = int(input("ingrese su año de nacimiento: "))
Nhijos = int(input("ingrese su numero de hijos: "))
años_en_banco = int(input("ingrese la cantidad de años en el banco: "))
estado_civil = input("ingrese su estado civil (S/C): ")
localidad = input("ingrese si vive en campo o ciudad(U/R): ")

if años_en_banco > 10 and Nhijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and Nhijos > 3 and 1974 >= año_nacimiento >= 1984:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and localidad == "U":
    print("APROBADO")
elif ingreso > 3500000 and años_en_banco > 5:
    print("APROBADO")
elif localidad == "R" and estado_civil == "C" and Nhijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
