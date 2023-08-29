#Aprobación de créditos
ingreso = int(input("ingrese su renta: "))
nacimiento = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese la cantidad de hijos: "))
pertenencia = int(input("ingrese su los años de pertenencia al banco: "))
estado = str(input("ingrese su estado civil ('C' Casado, 'S' Soltero): "))
vivienda = str(input("ingrese su vivienda ('U' Urbano, 'R' Rural): "))

edad = 2021 - nacimiento

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado == "C" and hijos > 3 and (edad >= 45 and edad <= 55):
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")     