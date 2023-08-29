##-Ingreso (en pesos)
##-Año de nacimiento
##-Número de hijos
##-Años de pertenencia al banco
##-Estado civil ("S": soltero, "C", casado)
##-Si vive en campo o cuidad ("U": urbano, "R": rural)
##-El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:
##
##-Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
##-Si el cliente es casado,tiene más de tres hijos, y tiene entre 45 y 55 años.
##-Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
##-Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
##-Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
##                    Tu programa debe preguntar sus datos al cliente, procesarlos,
##                    e imprimir el mensaje APROBADO o RECHAZADO según corresponda




I = int(input('Ingreso (en pesos): '))
F = int(input('Año de nacimiento(Ej: 1980 o 2000): '))
H = int(input('Número de hijos: '))
A = eval(input('Años de pertenencia al banco: '))
E = input('Estado civil ("S": soltero, "C", casado): ')
V = input('Si vive en campo o cuidad ("U": urbano, "R": rural): ')

S = 1
C = 2
U = 3
R = 4
AÑOS = F-2020

if A >= 10 and H>= 2:
    print('APROBADO')
elif E == 2 and  H > 3 and 45 <= AÑOS >= 55:
    print('APROBADO')

elif I >= 2500000 and E == 1 and U == 3:
    print('APROBADO')

elif I >= 3500000 and A>5:
    print('APROVADO')
elif R == 4 and C==2 and 0 <= H < 2:
    print('APROBADO')


else:
    print('RECHAZADO')


      