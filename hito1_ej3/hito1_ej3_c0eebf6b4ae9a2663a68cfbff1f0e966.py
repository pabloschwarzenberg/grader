#Aprobación de créditos
ingresos = int(input("ingrese su ingreso en pesos -> $  "))
fecha = eval(input("ingrese su año de nacimiento -> "))
hijos = eval(input("ingrese la cantidad total de hijos ->")) 
AñosBanco =int(input("cuantos años lleva siendo socio del banco -> "))
estado_Civil = input("S.soltero  C.casado ->  ")
residencia = input("ingrese su lugar de residencia campo o cuidad U.urbano, R.rural -> ")
urbano = "U"
rural = "R" 
soltero = "S"
casado = "C"
año_actual = 2020
x = int(año_actual - fecha)
if AñosBanco == 10 or hijos == 2 :
    print("CREDITO APROBADO")
else: 
    print("CREDITO RECHAZADO")
if estado_Civil == "C" or hijos > 3 and x > 45 and x <= 55 :
    x = int(año_actual - fecha)
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")
if ingresos > 2500000 or estado_Civil == "S" or residencia == "U" :
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")
if ingresos > 3500000 or AñosBanco > 5 :
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")
if residencia == "R" or estado_Civil== "C" or hijos < 2 :
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")