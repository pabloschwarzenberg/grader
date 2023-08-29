#Aprobación de créditos
ingreso=int(input("Ingreso: "))
nacimiento=int(input("Año de nacimiento: "))
hijos=int(input("Numero de hijos: "))
AB=int(input("Años de pertenencia al banco: "))
EC=input("Estado civil: ")
vivienda=input("Rural o Urbano: ")

if AB>10 and hijos>=2:
    print("APROBADO")
if EC=="C" and hijos>3 and 1961<=nacimiento<=1971:
    print("APROBADO")
if ingreso>=2500000 and EC=="S" and vivienda=="U":
    print("APROBADO")
if ingreso>=3500000 and AB>5:
    print("APROBADO")
if vivienda=="R" and EC=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")