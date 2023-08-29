#Aprobación de créditos
ingre = int(input('Ingresos del postulante: '))
a_nac = int(input('Año de nacimiento: '))
n_hij = int(input('Número de hijos: '))
a_per = int(input('Años de pertenencia al banco: '))
e_civ = input("Estado civil ('S': soltero, 'C': casado)") 
lugar = input("Vive en campo o ciudad? ('U': urbano, 'R': rural): ")

edad = 2020 - a_nac

# CONDICIONES: 
con1 = a_per >= 10 and n_hij >= 2 

con2 = e_civ == 'C' and n_hij > 3 and (edad>=45 and edad <= 55) 

con3 = ingre < 2500000 and e_civ == 'S' and lugar == 'U'

con4 = ingre > 3500000 and a_per > 5

con5 = e_civ == 'C' and lugar == 'R' and n_hij < 2

credito = ' '
if con1 or con2 or con3 or con4 or con5:
    credito = 'APROBADO'

else:
    credito = 'RECHAZADO'

print(credito)