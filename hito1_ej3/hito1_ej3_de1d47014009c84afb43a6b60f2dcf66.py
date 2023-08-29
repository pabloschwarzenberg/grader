#Aprobación de créditos
S = 1
C = 2
U = 3
R = 4

I = eval(input('Ingresos:'))
X = eval(input('Año de nacimiento:'))
H = eval(input('Número de hijos:'))
A = eval(input('Años de pertenencia al banco:'))
EC = eval(input('Estado civil(S o C):'))
V = eval(input('Vive en campo o cuidad(U O R):'))

edad = 2020 - X

if (A > 10) and (H >= 2):
    print('APROBADO')
    
elif (EC == C) and (H > 3) and (45 < edad < 55):
    print('APROBADO')
    
elif (I >= 250000) and (EC == 1) and (V == 2):
    print('APROBADO')
    
elif (I > 3500000) and A >= 5:
    print('APROBADO')
    
elif V == 4 and EC == 2 and H < 2:
    print('APROBADO')
    
else:
    print('RECHAZADO')
                
                