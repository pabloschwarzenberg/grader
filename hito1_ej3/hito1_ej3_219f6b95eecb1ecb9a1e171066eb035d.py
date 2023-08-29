#Aprobación de créditos
ingreso = int(input("Ingreso (en pesos): "))
ano_nac = int(input("Año de nacimiento: "))
num_hijos = int(input("Número de hijos: "))
anos_pert_banco = int(input("Años de pertenencia al banco: "))
est_civil = input("Estado civil ('S': soltero, 'C', casado): ")
vivienda = input("Si vive en campo o cuidad ('U': urbano, 'R': rural): ")
edad = 2020-ano_nac
if anos_pert_banco>10 and num_hijos>=2:
    print("APROBADO")
elif est_civil=='C' and num_hijos>3 and 45<=edad<=55:
    print("APROBADO")
elif ingreso>2500000 and est_civil=='S' and vivienda=='U':
    print("APROBADO")
elif ingreso>3500000 and anos_pert_banco>5:
    print("APROBADO")
elif vivienda=='R' and est_civil=='C' and num_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")