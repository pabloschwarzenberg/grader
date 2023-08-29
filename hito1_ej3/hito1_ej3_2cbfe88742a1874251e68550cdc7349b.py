#Aprobación de créditos

ingreso = float(input("Ingreso (en pesos): "))
año_nacimiento = int(input("Ingreso año de nacimiento: "))
hijos = int(input("Ingreso número de hijos: "))
años_banco = int(input("Ingreso años de pertenencia al banco: "))
estado_civil = input('Ingreso estado civil ("S": soltero, "C":casado) ' )
ubicacion = input('Campo o ciudad ("U":urbano, "R":rural) ' )

edad = 2020-año_nacimiento

if años_banco>10 and hijos >=2: 
    print("APROBADO")
elif estado_civil == "C" and hijos>=3 and edad>=45 and edad<=55:
    print("APROBADO")
elif estado_civil == "S" and ingreso>2500000 and ubicacion=="U":
    print("APROBADO")
elif años_banco >5  and ingreso>3500000:
    print("APROBADO")
elif ubicacion=="R" and estado_civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")