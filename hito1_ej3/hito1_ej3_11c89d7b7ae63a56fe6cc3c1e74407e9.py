#Aprobación de créditos
ingreso = int(input("ingrese el valor de tus ingresos en pesos: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Número de hijos: "))
pertenencia = int(input("Años de pertenencia al banco(Solo el número de años): "))
estadocivil = input("soltero o casado (S o C): ")
vivienda = input("campo o ciudad ( U O R): ")

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")

if estadocivil=="C" and hijos >3 and nacimiento in range(1966, 1976):
        print("APROBADO")

if ingreso >= 2500000 and estadocivil=="S"  and vivienda=="U":
    print("APROBADO")

if ingreso> 3500000 or pertenencia >5:
    print("APROBADO")

if vivienda== "R" and estadocivil=="C" and hijos<2:
     print("APROBADO")
else:
    print("RECHAZADO")