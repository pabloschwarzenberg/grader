ingreso = int(input("Ingresa el valor de tus ingresos en pesos: "))
nacimiento = int(input("Año en el que naciste: "))
hijos = int(input("Número de hijos: "))
pertenencia = int(input("Años de pertenencia al banco(Solo el número de años): "))
estado = input("soltero o casado (S o C): ")
vivienda = input("urbano o rural ( U O R): ")

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")

if estado=="C" and hijos >3 and nacimiento in range(1966, 1976):
        print("APROBADO")

if ingreso >= 2500000 and estado=="S"  and vivienda=="U":
    print("APROBADO")

if ingreso> 3500000 or pertenencia >5:
    print("APROBADO")

if vivienda== "R" and estado=="C" and hijos<2:
     print("APROBADO")
else:
    print("RECHAZADO")