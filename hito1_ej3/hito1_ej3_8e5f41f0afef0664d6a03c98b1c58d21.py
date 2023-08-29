#Aprobación de créditos
 ingreso = int(input("Ingresos: $ "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
pertenencia = int(input("Pertenencia al banco: "))
estado_civil = input("Estado civil S o C: ")
vivienda = input("Urbano o rural U o R: ")

edad = 2022 - nacimiento

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and hijos > 3 and edad >=45 and edad <=55:
    print("APROBADO")
elif ingreso > 250000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")