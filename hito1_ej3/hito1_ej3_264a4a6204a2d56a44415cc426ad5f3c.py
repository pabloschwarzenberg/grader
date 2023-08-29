#Aprobación de créditos
ingresos = eval(input("Ingreses sus incresos por favor: "))
año_nacimiento = eval(input("Ingrese el Año en el que nació por favor: "))
nh = eval(input("Ingrese el numero de hijos por favor: "))
años_banco = eval(input("Ingreses sus Años en el banco por favor: "))
ec = str(input("Ingrese su estado civil (Soltero = S ; Casado = C) por favor: "))
vive = str(input("Ingrese como es su zona donde vive si es (rural = R ; urbana = U) por favor: "))

if((años_banco >= 10) and (nh >= 2)):
    print("APROBADO")
elif((ec == "C") and (nh >= 3) and (año_nacimiento >= 1975 and año_nacimiento <= 1965)):
    print("APROBADO")
elif((ingresos >= 2500000) and (ec == "S") and (vive == "U")):
    print("APROBADO")
elif((ingresos >= 3500000) and (años_banco == 5)):
    print("APROBADO")
elif((vive == "R") and (ec == "C") and (nh < 2)):
    print("APROBADO")
else:
    print("RECHAZADO")