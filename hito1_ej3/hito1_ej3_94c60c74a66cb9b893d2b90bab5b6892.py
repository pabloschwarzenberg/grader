print("Bienvenido al banco. Por favor, rellene los siguientes datos.")

credito = "RECHAZADO"

ingreso = int(input('Su ingreso (en pesos): '))
nacimiento = int(input('Su anho de nacimiento: '))
hijos = int(input('Numero de hijos: '))
pertenencia = int(input('Anhos de pertenencia al banco: '))
estado = input('Su estado civil ("S": Soltero, "C": Casado): ')
vivienda = input('Su lugar de residencia ("U": Urbano, "R": Rural): ')

if(pertenencia > 10 and hijos >= 2): credito = "APROBADO"
elif(estado == "C" and hijos > 3 and (2021-nacimiento >= 45 and 2021-nacimiento <= 55)): credito = "APROBADO"
elif(ingreso > 2500000 and estado == "S" and vivienda == "U"): credito = "APROBADO"
elif(ingreso > 3500000 and pertenencia > 5): credito = "APROBADO"
elif(vivienda == "R" and estado == "C" and hijos < 2): credito = "APROBADO"

print("Su credito ha sido " + credito)