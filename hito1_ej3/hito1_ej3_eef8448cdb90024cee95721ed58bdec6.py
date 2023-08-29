#Aprobación de créditos
ingreso = int(input('Escriba sus ingresos en pesos'))
nacimiento = int(input('Escriba su año de nacimiento'))
hijos = int(input('Ingrese numero de hijos'))
pertenencia = int(input('Ingrese años de pertenencia al banco'))
estado = input('Ingrese su estado civil. S = Soltero, C = Casado')
vivienda = input('Ingrese si vive en campo o ciudad U = Urbano, R = Rural')

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado == 'C' and hijos > 3 and 2021 - nacimiento >= 45 and 2021 - nacimiento <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      