import datetime

ingreso=int(input("Ingreso en pesos: "))
an_nacimiento=int(input("Año de nacimiento: "))
an_actual=datetime.datetime.now().year
num_hijos=int(input("Número de hijos: "))
ant_cliente=int(input("Años de pertenencia al banco: "))
e_civil=str(input("Estado civil ('S': soltero, 'C'', casado): ")[0]).upper()
ur=str(input("Si vive en campo o cuidad ('U': urbano, 'R'': rural): ")[0]).upper()
edad=int(an_actual-an_nacimiento)

if (((ant_cliente>10) and (num_hijos>1)) or ((e_civil=="C") and (num_hijos>3) and (45<=(edad)<=55)) or ((ingreso>2500000) and (e_civil=="S") and (ur=="U")) or ((ingreso>3500000) and (ant_cliente>5)) or ((ur=="R") and (e_civil=="C") and (num_hijos<2))):
    print("APROBADO")
else:
    print("RECHAZADO")
