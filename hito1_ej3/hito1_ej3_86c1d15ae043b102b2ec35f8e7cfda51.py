ingreso=eval(input("Introduzca sus ingresos:"))
anho=eval(input("Introduzca su año de nacimiento:"))
numero_de_hijos=eval(input("Introduzca su numero de hijos:"))
anho_de_pertenencia_banco=eval(input("Introduzca el año de pertenecia del banco:"))
estado_civil=str(input("Introduzca el estado civil(S o C):"))
vivienda=str(input("Introduzca donde vive(U o R):"))

if anho_de_pertenencia_banco>10 and numero_de_hijos>=2:
    print("APROBADO")
elif estado_civil == "C" and numero_de_hijos>3 and anho>45 and anho<55:
    print("APROBADO")
elif ingreso>2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso>3500000 and anho_de_pertenencia_banco>5:
    print("APROBADO")
elif vivienda == "R" and estado_civil ==  "C" and numero_de_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")