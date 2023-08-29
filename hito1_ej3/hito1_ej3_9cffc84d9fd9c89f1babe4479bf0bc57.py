#Aprobación de créditos
      ingresos   = int(input("Ingreso (en pesos): "))
nacimiento = int(input("Año de nacimiento: "))
hijos      = int(input("Número de hijos: "))
tiempo     = int(input("Años de pertenencia al banco: "))
estado     = input("Estado civil ('S': soltero, 'C', casado): ")
vivienda     = input("Si vive en campo o cuidad ('U': urbano, 'R': rural): ")

edad = ( 2020 - nacimiento)


if tiempo > 10 and hijos >= 2 :
    print("APROBADO")
elif estado == "c" or estado == "C" and hijos >3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingresos > 2500000 and  estado == "S" and  vivienda == "U" :
    print("APROBADO")
elif ingresos > 3500000 and tiempo > 5 :
    print ("APROBADO")
elif vivienda == "R" and estado == "C" and hijos < 2 :
    print ("APROBADO")
else :
    print ("RECHAZADO")