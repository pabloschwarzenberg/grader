#Aprobación de créditos
#n = numero
ingresos = eval(input("introduzca sus ingresos:"))
anho = eval(input("introduzca su año de nacimiento"))
n_de_hijos = eval(input("introduzca el numero de hijos:"))
anho_de_pertenencia_banco = eval(input("introduzca el año de pertenencia:"))
estado_civil = str(input("introduzca su estado civil (C o S)"))
vivienda = str(input("introduzca donde vive (U o R)"))

if anho_de_pertenencia_banco > 10 and n_de_hijos >= 2:
    print("APROBADO")

elif estado_civil == "C" and n_de_hijos > 3 and anho > 45 and anho < 55:
    print("APROBADO")

elif ingresos > 2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")

elif ingresos > 3500000 and estado_civil == "C" and anho_de_pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and n_de_hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")      