#Aprobación de créditos
I = float(input('Introdusca ingresos en pesos: '))
A = float(input('Introdusca año de nacimiento: '))
N = float(input('Introdusca número de hijos: '))
AB = float(input('Introdusca años de pertenencia al banco: '))
EC = input('Introdusca su estado civil, es decir S (soltero) o C (casado): ')
UR = input('Introdusca U (urbano) si vive en ciudad o R (rural) si vive en campo: ')
Edad = 2020 - A
EC_str = str(EC)
UR_str = str(UR)
if (AB > 10 and N >= 2) or (EC_str == 'C' and N > 3 and Edad in range(45,55)) or (I > 2500000 and EC_str == 'S' and UR_str == 'U') or (I > 3500000 and AB > 5) or (UR_str == 'R' and EC_str == 'C' and N < 2):
 print('APROBADO')
else:
 print('RECHAZADO')