ingresos = eval(input("Ingreso (en pesos): "))
nacimiento = eval(input("Año de nacimiento: "))
hijos = eval(input("Número de hijos: "))
años = eval(input("Años de pertenencia al banco: "))
estado_civil = input("Estado civil ((S): soltero, (C): casado): ")
direccion = input("Si vive en campo o cuidad ((U): urbano, (R): rural): ")

edad = 2022-nacimiento

condicion1 = (años >=10) and (hijos >=2)
condicion2 = (estado_civil == 'C') and (hijos >=3) and (edad >=45<=55)
condicion3 = ingresos >= 2500000 and estado_civil == 'S' and direccion == 'U'
condicion4 = ingresos >= 3500000 and años >=5
condicion5 = direccion == 'R' and estado_civil == 'C' and hijos <=1

comprobacion = condicion1 or condicion2 or condicion3 or condicion4 or condicion5

if comprobacion is True:
    print ("APROBADO")
else:
    print ("RECHAZADO")